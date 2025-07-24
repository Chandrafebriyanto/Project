# list casting adalah mengubah tipe data lain menjadi list
# contoh mengubah tuple, string, dan range menjadi list

my_tuple = (10, 20, 30)
my_string = "python"
my_range = range(1,6)

my_tuple_list = list(my_tuple)
my_string_list = list(my_string)
my_range_list = list(my_range)

print(my_tuple_list)  # Output: [10, 20, 30]
print(my_string_list)  # Output: ['p', 'y', 't', 'h', 'o', 'n']
print(my_range_list)  # Output: [1, 2, 3, 4, 5]