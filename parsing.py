from classes import Library
from classes import Task

import pickle

files = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']

for file in files:
    file_name = 'data/' + file
    with open(file_name) as input_f:
        lines = input_f.readlines()

    libraries = []
    for (i, line) in enumerate(lines):
        if i == 0:
            words = line.split()
            num_of_books = int(words[0])
            num_of_libraries = int(words[1])
            scanning_days = int(words[2])
        elif i == 1:
            book_scores = list(map(int, line.split()))
        elif i % 2 == 0:
            if i > num_of_libraries*2:
                break
            words = line.split()
            num_of_books_in_lib = int(words[0])
            sign_up_duration = int(words[1])
            books_per_day_shipping = int(words[2])
            lib = Library(num_of_books_in_lib, sign_up_duration, books_per_day_shipping, list(map(int, lines[i+1].split())))
            libraries.append(lib)


    task = Task(num_of_books=num_of_books, num_of_libraries=num_of_libraries, scanning_days=scanning_days, libraries=libraries, book_scores=book_scores)

    pickle_out = open( file + ".pickle", "wb")
    pickle.dump(task, pickle_out)
    pickle_out.close()





