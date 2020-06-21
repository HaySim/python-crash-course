# prints only the numbers 1 through 4:
# 1
# 2
# 3
# 4 
for value in range(1, 5):
    print(value)

# [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)

# starts with value 2 and then adds 2 to that value until it reaches or passes the end value, 11:
# [2, 4, 6, 8, 10]
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# putting the first 10 square numbers into a list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# writing this code more concisely:
# the code in line 30 does the same work as the lines 22 and 23. 
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

numbers = list(range(1, 21))
print(numbers)

cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)