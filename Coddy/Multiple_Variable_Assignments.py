#multiple variable assignments adalah sebuah teknik dalam pemrograman
# yang memungkinkan kita untuk menetapkan beberapa variabel
# dalam satu baris kode. Ini berguna untuk membuat kode lebih ringkas
# dan mudah dibaca, terutama ketika kita memiliki beberapa variabel

# Example:
a, b, c = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

x = y = z = 10
print(x)  # Output: 10
print(y)  # Output: 10
print(z)  # Output: 10

numbers = [4, 5, 6]
a, b, c = numbers
print(a)  # Output: 4
print(b)  # Output: 5
print(c)  # Output: 6


# tittle: Multiple Variable Assignments Example
# Assign values to name, age, and city
name,age,city = ('Alice', 30, 'New York')

# Assign 100 to x, y, and z
x = y = z = 100

# Create a list of colors and assign them to color1, color2, and color3
colors = ["red", "green", "blue"]
color1, color2, color3 = colors

# Don't change the code below
print(f"Name: {name}, Age: {age}, City: {city}")
print(f"x: {x}, y: {y}, z: {z}")
print(f"Colors: {color1}, {color2}, {color3}")