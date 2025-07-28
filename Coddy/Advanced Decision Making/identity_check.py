list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 == list2:
    print(True)
if list1 is not list2:
    print(False)


list1 = [1, 2, 3]
list2 = list1

if list1 == list2:
    print(True)
if list1 is list2:
    print(True)

