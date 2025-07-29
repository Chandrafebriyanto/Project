def remove_duplicates(numbers):
    my_set = set(numbers)
    return list(my_set)


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))