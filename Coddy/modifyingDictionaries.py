# modifying dictionaries adalah cara untuk mengubah, menambah, atau menghapus elemen dalam sebuah dictionary.

# tittle: adding a new key-value pair
# Start with an empty dictionary
my_dict = {}

# Add a new key-value pair
my_dict["name"] = "Alice"
my_dict["age"] = 30

print(my_dict)
# Output: {'name': 'Alice', 'age': 30}  

# tittle: updating an existing key-value pair
# Update the age
my_dict["age"] = 31

print(my_dict)
# Output: {'name': 'Alice', 'age': 31}

# tittle: removing a key-value pair
# Delete the age
del my_dict["age"]

print(my_dict)
# Output: {'name': 'Alice'}


# EXAMPLE:
def update_employee_info(employee_dict, key, value):
    dictionary = employee_dict
    dictionary[key] = value
    return dictionary

result = update_employee_info({"name": "John", "age": 30}, "age", 31)
print(result) 
