# set mathematical Operation adalah operasi yang memungkinkan untuk membandingkan atau menggabungkan 2 elemen atau lebih set bedasarkan elemen yang ada di dalamnya

# Union (menggabungkan)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)
# Output: {1, 2, 3, 4, 5}

# Intersection (irisan)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)
# Output: {3}

# Difference (selisih)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)
# Output: {1, 2}

# Symmetric Difference (Selisih simetris)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)
# Output: {1, 2, 4, 5}


# EXAMPLE :
def set_operations(set1, set2):
    # Calculate the union
    union_result = set1 | set2

    # Calculate the intersection
    intersection_result = set1 & set2

    # Calculate the difference
    difference_result = set1 - set2

    # Calculate the symmetric difference
    symmetric_difference_result = set1 ^ set2

    # Return a dictionary containing the results
    return {
        "union": union_result,
        "intersection": intersection_result,
        "difference": difference_result,
        "symmetric_difference": symmetric_difference_result
    }

print(set_operations({1, 2, 3}, {3, 4, 5}))



group1 = {"Alice", "Bob", "Charlie", "Diana"}
group2 = {"Bob", "Charlie", "Eve"}
group3 = {"Charlie", "Frank", "Bob"}

# Write your code below
intersection_result = group1 & group2 & group3
difference_result = group1 - group2 - group3

# Print the results
print("Members in all groups:", sorted(list(intersection_result)))
print("Unique members in group1:", sorted(list(difference_result)))


region1 = {"gold coin", "ruby", "emerald", "pearl"}
region2 = {"ruby", "emerald", "sapphire"}
region3 = {"emerald", "diamond", "sapphire"}

# Write code here
shared_treasures = region1 & region2 & region3
unique_treasures_region1 = region1 - region2 - region3
all_treasures = region1 | region2 | region3
exclusive_treasures = (region1 - region2 - region3) | (region2 - region1 - region3) | (region3 - region1 - region2)
#output = {"gold coin", "pearl", " diamond"}

# Print the results
print("Shared treasures:", sorted(list(shared_treasures)))
print("Unique treasures in region1:", sorted(list(unique_treasures_region1)))
print("All treasures:", sorted(list(all_treasures)))
print("Exclusive treasures:", sorted(list(exclusive_treasures)))