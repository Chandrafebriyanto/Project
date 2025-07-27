# dictionary adalah struktur data yang menyimpan pasangan kunci-nilai

# Step 1: Create the Grades Dictionary
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Step 2: Access All Keys and Values
print("Students:", grades.keys())  # Accessing all keys
print("Grades:", grades.values())  # Accessing all values
print("Group:", grades.items())  # Accessing all values

# Step 3: Add a New Student
grades["Diana"] = 92  

# Step 4: Retrieve a Student's Grade
grade = grades["Bob"]  # Accessing Bob's grade
print("Bob's grade:", grade)

# Step 5: Remove a Student
remove = grades.pop("Charlie")
print(f"Updated grades: {grades}")



# output:
# Students: dict_keys(['Alice', 'Bob', 'Charlie'])
# Grades: dict_values([85, 90, 78])
# Bob's grade: 90
# Updated grades: {'Alice': 85, 'Bob': 90, 'Diana': 92}
