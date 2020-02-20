#!/usr/bin/python

from ortools.graph import pywrapgraph
import classes

# assume that solution has lib_ordering
def fill_books_and_score(task, solution):
	current_day = 0
	library_nodes = {}
	book_node = {}
	start_nodes = []
	end_nodes = []
	capacities = []
	unit_costs = []
	source_node = 0
	sink_node = 1
	next_node = 2
	supplies = []
	start_nodes.append(sink_node)
	end_nodes.append(source_node)
	capacities.append(len(task.book_scores))
	unit_costs.append(0)
	for book in range(len(task.book_scores)):
		book_node[book] = next_node
		next_node += 1
		start_nodes.append(book_node[book])
		end_nodes.append(sink_node)
		capacities.append(1)
		unit_costs.append(-task.book_scores[book])
	for lib in solution.lib_ordering:
		current_day += task.libraries[lib].sign_up_duration
		if current_day > task.scanning_days: break
		books_from_here = (task.scanning_days - current_day) * task.libraries[lib].books_per_day_shipping
		if books_from_here <= 0: break
		library_nodes[lib] = next_node
		next_node += 1
		start_nodes.append(source_node)
		end_nodes.append(library_nodes[lib])
		capacities.append(books_from_here)
		unit_costs.append(0)
		for book in task.libraries[lib].book_list:
			start_nodes.append(library_nodes[lib])
			end_nodes.append(book_node[book])
			capacities.append(1)
			unit_costs.append(0)
	for i in range(0, next_node):
		supplies.append(0)
	rev_library_node = {}
	rev_book_node = {}
	for k in library_nodes:
		rev_library_node[library_nodes[k]] = k
	for k in book_node:
		rev_book_node[book_node[k]] = k
	min_cost_flow = pywrapgraph.SimpleMinCostFlow()
	for i in range(0, len(start_nodes)):
		min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_costs[i])
	for i in range(0, len(supplies)):
		min_cost_flow.SetNodeSupply(i, supplies[i])
	assert len(start_nodes) == len(end_nodes)
	assert len(end_nodes) == len(capacities)
	assert len(capacities) == len(unit_costs)
	assert len(supplies) == next_node
	solved = min_cost_flow.SolveMaxFlowWithMinCost()
	if solved != min_cost_flow.OPTIMAL:
		print("error solving the flow?")
		print(solved)
	solution.books_per_library = []
	for i in range(0, len(solution.lib_ordering)):
		solution.books_per_library.append([])
	solution.scores = 0
	for i in range(min_cost_flow.NumArcs()):
		if min_cost_flow.Tail(i) in rev_library_node and min_cost_flow.Head(i) in rev_book_node:
			if min_cost_flow.Flow(i) > 0:
				lib = rev_library_node[min_cost_flow.Tail(i)]
				book = rev_book_node[min_cost_flow.Head(i)]
				solution.books_per_library[lib].append(book)
		if min_cost_flow.Tail(i) in rev_book_node and min_cost_flow.Head(i) == sink_node:
			if min_cost_flow.Flow(i) > 0:
				solution.scores -= min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
