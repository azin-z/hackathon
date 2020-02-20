#!/usr/bin/python

import score_solution
import classes

libs = []
libs.append(classes.Library(5, 2, 2, [0, 1, 2, 3, 4]))
libs.append(classes.Library(4, 3, 1, [3, 2, 5, 0]))
task = classes.Task(6, 2, 7, libs, [1, 2, 3, 6, 5, 4])
solution = classes.Solution([1, 0])

score_solution.fill_books_and_score(task, solution)

assert solution.scores == 21
assert len(solution.books_per_library) == 2
solution.books_per_library[0].sort()
solution.books_per_library[1].sort()
assert solution.books_per_library[0] == [1, 2, 3, 4]
assert solution.books_per_library[1] == [0, 5]
