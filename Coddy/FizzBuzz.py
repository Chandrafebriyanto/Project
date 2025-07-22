num = int(input())
print("Welcome to FizzBuzz!")
def fizzbuzz(n):
    string_num = str(n)
    if (n % 3 == 0 and n % 7 == 0):
        return "FizzBuzz"
    elif (n % 3 == 0):
        return "Fizz"
    elif (n % 7 == 0):
        return "Buzz"
    else:
        if ("3" in string_num):
            return "Almost Fizz"
        else:
            return string_num


for i in range (1, num + 1):
    print(fizzbuzz(i))
