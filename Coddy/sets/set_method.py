# discrad adalah menghapus element spesifik dari set
my_set = {1, 2, 3}
my_set.discard(3)    # Removes 3 from the set
my_set.discard(4)    # No error, even though 4 is not in the set
print(my_set)
# Output: {1, 2}

# pop adalah menghapus element paling kiri/depan 
my_set = {1, 2, 3}
element = my_set.pop()  # Removes and returns an arbitrary element
print(element)
# Output: 1 (or another element, as it's arbitrary)
print(my_set)
# Output: {2, 3} (or a different set, depending on the popped element)

# clear adalah menghapus semua data yang ada dalam set
my_set = {1, 2, 3}
my_set.clear()       # Removes all elements
print(my_set)
# Output: set()


# Write code here
numbers = {10,20,30,40,50}
numbers.discard(35)
print(numbers)

popped_element = numbers.pop()
print(popped_element)

numbers.clear()
print(numbers)