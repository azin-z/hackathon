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


