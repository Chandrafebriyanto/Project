# adding set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Output: {1, 2, 3, 4}

# remove set
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# Output: {1, 3}

# check set
my_set = {1, 2, 3}
print(2 in my_set)
# Output: True
print(4 in my_set)
# Output: False


def manage_set(set1, element_to_add, element_to_remove):
    set1.add(element_to_add)
    if element_to_remove in set1:
        set1.remove(element_to_remove)
    if 5 in set1:
        return "5 is in the set"
    else:
        return "5 is not in the set"

print(manage_set({1,2,3,4,5,6}, 7, 8))