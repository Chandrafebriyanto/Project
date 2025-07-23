#Challenges 1:Flat Asterisk Pyramid
n = int(input())
rows = int(n/2)+1
for i in range(rows):
    print("*" * (2 * i + 1))


#tittle: Challenges 2: Pattern Finder
def find_occurrences(text, pattern):
    if pattern in text:
        count = 0
        lst = []
        for i in range(len(text)):
            if text[i:i+len(pattern)] == pattern:
                lst.append(i)
                count += 1
        return (True, count, lst)
    else:
        return((False, 0, []))

# Read input
text = input()
pattern = input()
# Example input:
# text = "ababcabcabababd"
# pattern = "abab"

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)


#tittle: Challenges 3:What To Buy
prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0

for i in range(len(prices)):
    if prices[i] <= budget_per_item:
        affordable_items.append(items[i])
        total_needed += prices[i]
    else:
        cant_afford += 1

# input example:
# 10,25,5,15
# hummer,saw,nails,brush
# 12

print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
