def frequency_counter(data_list):
    frequency = {}
    for item in data_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

# Example usage
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
result = frequency_counter(data)
print(result)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}