import pickle
import score_solution
import classes


# files = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']
files = ['a_example.txt']


for file in files:
    pickle_in = open('task_pickles/' + file + ".pickle", "rb")
    task = pickle.load(pickle_in)
    solution = classes.Solution([1, 0])

    score_solution.fill_books_and_score(task, solution)

    assert solution.scores == 21
    assert len(solution.books_per_library) == 2
    solution.books_per_library[0].sort()
    solution.books_per_library[1].sort()
    assert solution.books_per_library[0] == [1, 2, 3, 4]
    assert solution.books_per_library[1] == [0, 5]