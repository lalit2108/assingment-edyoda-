list_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_tuples = sorted(list_tuples, key=lambda x: x[-1])

print(sorted_tuples)