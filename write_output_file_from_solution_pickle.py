import pickle

files = ['a_example', 'b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']
# files = ['a_example']

for file in files:
    solution_pickle_in = open('solution_pickles/' + file + '.pickle', "rb")
    solution = pickle.load(solution_pickle_in)
    with open('solution_output_files/' + file + '.txt', 'w') as output_file:
        print(len([lib for lib in solution.lib_ordering if len(solution.books_per_library[lib]) > 0]), file=output_file)
        for (i, lib) in enumerate(solution.lib_ordering):
            if len(solution.books_per_library[lib]) == 0:
                continue
            print(lib, len(solution.books_per_library[lib]), file=output_file)
            print(" ".join(str(item) for item in solution.books_per_library[lib]), file=output_file)

