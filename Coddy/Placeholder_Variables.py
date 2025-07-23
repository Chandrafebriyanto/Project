# placeholder_variables adalah variabel yang digunakan untuk menyimpan nilai sementara
# sebelum nilai sebenarnya ditetapkan. Ini berguna dalam situasi di manakita perlu menyiapkan struktur data atau algoritma sebelum mengisi nilai yang sebenarnya.


# EXAMPLE:
# Loop 5 times using a placeholder variable
for _ in range(5):
    print("Iteration")    
    
# List of numbers
numbers = [10, 20, 30, 40, 50]

# Unpack the list using placeholder variables
first, _, middle, _, last = numbers

# Print the values of first, middle, and last
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")