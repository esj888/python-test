# 26.1 squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [x*x for x in numbers]
print(squared_numbers)

# 26.2 exercise 2 - even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [x for x in numbers if x % 2 == 0]
print(result)

# 26.3
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# import fileinput
file1 = open("file1.txt")
file2 = open("file2.txt")
file1_list = file1.readlines()
file2_list = file2.readlines()
result2 = [int(x) for x in file1_list if x in file2_list]
print(file1_list)
print(file2_list)
print(result2)
file1.close()
file2.close()
