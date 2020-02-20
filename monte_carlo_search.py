#!/usr/bin/python

import pickle
import score_solution
import classes
import parsing
import sys
import random
import subprocess

input_problem_pickle = sys.argv[1]
output_solution_pickle = sys.argv[2]
print(input_problem_pickle)
print(output_solution_pickle)

def generate_libray_permutation(n):
	order = []
	for i in range(n):
		order.append(i)
	random.shuffle(order)
	return order

with open(input_problem_pickle, "rb") as pickle_in:
	task = pickle.load(pickle_in)

try:
	with open(output_solution_pickle, "rb") as pickle_in:
		best_solution = pickle.load(pickle_in)
except:
	best_solution = classes.Solution([0])
	best_solution.scores = -1

while True:
	new_order = generate_libray_permutation(len(task.libraries))
	new_solution = classes.Solution(new_order)
	score_solution.fill_books_and_score(task, new_solution)
	if new_solution.scores <= best_solution.scores: continue
	with open(output_solution_pickle + ".tmp", "wb") as pickle_out:
		pickle.dump(new_solution, pickle_out)
	best_solution = new_solution
	subprocess.run(["cp", output_solution_pickle + ".tmp", output_solution_pickle])
	subprocess.run(["rm", output_solution_pickle + ".tmp"])
	print("found solution with score: " + str(best_solution.scores))
