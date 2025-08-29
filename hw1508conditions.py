# 1. Check the sign of a number
num = float(input("Enter a number (to check its sign): "))
if num > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("negative")


# 2. Age category
age = int(input("Enter age: "))
if age < 18:
    print("minor")
elif 18 <= age <= 59:
    print("adult")
else:
    print("senior")


# 3. Check if a number is even or odd
num2 = int(input("Enter a number (check even/odd): "))
if num2 % 2 == 0:
    print("even")
else:
    print("odd")
