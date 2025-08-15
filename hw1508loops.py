# 1. Вивести всі числа від 1 до 100
print("Числа від 1 до 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n" + "-"*40)

# 2. Таблиця множення для числа, яке вводить користувач
num = int(input("Введіть число для таблиці множення: "))
print(f"Таблиця множення для {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("-"*40)

# 3. Сума чисел від 1 до N
N = int(input("Введіть N для суми 1..N: "))
total = 0
for i in range(1, N + 1):
    total += i
print(f"Сума чисел від 1 до {N} = {total}")
