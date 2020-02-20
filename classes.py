

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