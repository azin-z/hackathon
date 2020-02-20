#!/usr/bin/python

import pickle
import classes
import score_solution
import sys

input_problem_pickle = sys.argv[1]
output_solution_pickle = sys.argv[2]

with open(input_problem_pickle, "rb") as pickle_in:
	task = pickle.load(pickle_in)

used_books = set()
used_libraries = set()

order = []
days_left = task.scanning_days

def get_best_books(lib):
	days_here = days_left - task.libraries[lib].sign_up_duration
	if days_here <= 0: return []
	books = []
	for book in task.libraries[lib].book_list:
		if book not in used_books:
			books.append(book)
	books.sort(key = lambda x: task.book_scores[x], reverse = True)
	books_from_here = days_here * task.libraries[lib].books_per_day_shipping
	books = books[0:books_from_here]
	return books

def get_greedy_score(lib):
	books = get_best_books(lib)
	scoresum = 0
	for x in books:
		scoresum += task.book_scores[x]
	return scoresum

while True:
	best_greedy = -1
	best_greedy_addition = -1
	for i in range(0, len(task.libraries)):
		if i in used_libraries: continue
		score_here = get_greedy_score(i)
		if score_here > best_greedy_addition:
			best_greedy_addition = score_here
			best_greedy = i
	if best_greedy_addition <= 0: break
	assert best_greedy != -1
	order.append(best_greedy)
	used_libraries.add(best_greedy)
	for x in get_best_books(best_greedy):
		used_books.add(x)
	days_left -= task.libraries[best_greedy].sign_up_duration
	if days_left < 0: break

solution = classes.Solution(order)
score_solution.fill_books_and_score(task, solution)

print(solution.scores)

with open(output_solution_pickle, "wb") as pickle_out:
	pickle.dump(solution, pickle_out)

