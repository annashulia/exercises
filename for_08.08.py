n = int(input("Enter a number n: "))

total = 0

for i in range(1, n + 1):
    if i % 5 == 0:
        total += i

print("Sum of all numbers divisible by 5:", total)
