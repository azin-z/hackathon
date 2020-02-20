
file_name = 'a_example.txt'
with open(file_name) as input_f:
    lines = input_f.readlines()

for (i, line) in lines:
    if i==0:
        words = line.split()
        num_of_books = words[0]



class Library:
    num_of_books = 0

    def __init__(self, num_of_books, sign_up_duration, books_per_day_shipping, book_indexes):
        self.num_of_books = num_of_books
        self.sign_up_duration = sign_up_duration
        self.books_per_day_shipping = books_per_day_shipping
        self.book_indexes = book_indexes
