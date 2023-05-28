def square(num):
    return num ** 2


numbers = [4, 5, 2, 9]
squared_numbers = list(map(square, numbers))
print("Square the elements of the list:")
print(squared_numbers)