#!/usr/bin/python

from ortools.graph import pywrapgraph
import classes

# assume that solution has lib_ordering
def fill_books_and_score(task, solution):
	current_day = 0
	library_nodes = {}
	book_node = {}
	source_node = 0
	sink_node = 1
	next_node = 2
	supplies = []
	min_cost_flow = pywrapgraph.SimpleMinCostFlow()
	min_cost_flow.AddArcWithCapacityAndUnitCost(sink_node, source_node, len(task.book_scores), 0)
	for book in range(len(task.book_scores)):
		book_node[book] = next_node
		next_node += 1
		min_cost_flow.AddArcWithCapacityAndUnitCost(book_node[book], sink_node, 1, -task.book_scores[book])
	for lib in solution.lib_ordering:
		current_day += task.libraries[lib].sign_up_duration
		if current_day > task.scanning_days: break
		books_from_here = (task.scanning_days - current_day) * task.libraries[lib].books_per_day_shipping
		if books_from_here <= 0: break
		library_nodes[lib] = next_node
		next_node += 1
		min_cost_flow.AddArcWithCapacityAndUnitCost(source_node, library_nodes[lib], books_from_here, 0)
		for book in task.libraries[lib].book_list:
			min_cost_flow.AddArcWithCapacityAndUnitCost(library_nodes[lib], book_node[book], 1, 0)
	for i in range(0, next_node):
		supplies.append(0)
	rev_library_node = {}
	rev_book_node = {}
	for k in library_nodes:
		rev_library_node[library_nodes[k]] = k
	for k in book_node:
		rev_book_node[book_node[k]] = k
	for i in range(0, len(supplies)):
		min_cost_flow.SetNodeSupply(i, supplies[i])
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
