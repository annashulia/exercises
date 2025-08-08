n = int(input("Введіть число n: "))

total = 0

for i in range(1, n + 1):
    if i % 5 == 0:
        total += i

print("Сума всіх чисел, що діляться на 5:", total)