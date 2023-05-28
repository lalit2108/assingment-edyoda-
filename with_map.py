def triple(num):
    return num * 3


numbers = [1, 2, 3, 4, 5, 6, 7]
tripled_numbers = list(map(triple, numbers))
print("Triple of list numbers:")
print(tripled_numbers)