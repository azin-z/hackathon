
task = n
file_name = 'a_example.txt'
with open(file_name) as input_f:
    lines = input_f.readlines()

for (i, line) in lines:
    if i==0:
        words = line.split()
        num_of_books = words[0]
        num_of_libraries = words[1]
        scanning_days = words[2]
        break
    if i==1:



class Task:
    def __init__(self, num_of_books, sign_up_duration, books_per_day_shipping, book_list):
        self.num_of_books = num_of_books
        self.num_of_libraries = num_of_libraries
        self.scanning_days = scanning_days
        self.libraries = libraries
        self.books_scores = book_scores

class Solution:
    def __init__(self, lib_ordering):
        self.lib_ordering = lib_ordering
        self.books_per_library = []
        self.scores = None



class Library:

    def __init__(self, num_of_books, sign_up_duration, books_per_day_shipping, book_list):
        self.num_of_books = num_of_books
        self.sign_up_duration = sign_up_duration
        self.books_per_day_shipping = books_per_day_shipping
        self.book_list = book_list


def