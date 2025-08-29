# 1. Print all numbers from 1 to 100
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n" + "-"*40)

# 2. Multiplication table for a number entered by the user
num = int(input("Enter a number for the multiplication table: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("-"*40)

# 3. Sum of numbers from 1 to N
N = int(input("Enter N for the sum 1..N: "))
total = 0
for i in range(1, N + 1):
    total += i
print(f"Sum of numbers from 1 to {N} = {total}")
