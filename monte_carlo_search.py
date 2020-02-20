#!/usr/bin/python

import pickle
import score_solution
import classes
import parsing
import sys
import random
import subprocess
import time
import threading
import queue

num_threads = int(sys.argv[1])
input_problem_pickle = sys.argv[2]
output_solution_pickle = sys.argv[3]

print(num_threads)
print(input_problem_pickle)
print(output_solution_pickle)

initial_best_solution = None
solution_queue = queue.Queue(0)

def generate_libray_permutation(n):
	order = []
	for i in range(n):
		order.append(i)
	random.shuffle(order)
	return order

def run_montecarlo():
	best_here = initial_best_solution
	while True:
		new_order = generate_libray_permutation(len(task.libraries))
		new_solution = classes.Solution(new_order)
		score_solution.fill_books_and_score(task, new_solution)
		if new_solution.scores <= best_here.scores: continue
		with open(output_solution_pickle + ".tmp", "wb") as pickle_out:
			pickle.dump(new_solution, pickle_out)
		best_here = new_solution
		solution_queue.put(best_here)

def run_pick_best():
	global_best = initial_best_solution
	while True:
		new_solution = solution_queue.get()
		if new_solution.scores <= global_best.scores: continue
		with open(output_solution_pickle + ".tmp", "wb") as pickle_out:
			pickle.dump(new_solution, pickle_out)
		global_best = new_solution
		subprocess.run(["cp", output_solution_pickle + ".tmp", output_solution_pickle])
		subprocess.run(["rm", output_solution_pickle + ".tmp"])
		print("found solution with score: " + str(global_best.scores))

with open(input_problem_pickle, "rb") as pickle_in:
	task = pickle.load(pickle_in)

try:
	with open(output_solution_pickle, "rb") as pickle_in:
		initial_best_solution = pickle.load(pickle_in)
except:
	initial_best_solution = classes.Solution([0])
	initial_best_solution.scores = -1

start_time = time.time()
new_order = generate_libray_permutation(len(task.libraries))
new_solution = classes.Solution(new_order)
score_solution.fill_books_and_score(task, new_solution)
end_time = time.time()
print("One iteration takes " + str(end_time - start_time) + " seconds")

write_thread = threading.Thread(target=run_pick_best)
write_thread.start()

for i in range(0, num_threads):
	threadi = threading.Thread(target=run_montecarlo)
	threadi.start()

while True:
	pass # loop until closed
