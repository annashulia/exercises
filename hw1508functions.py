def add_numbers(a, b):
    """Повертає суму двох чисел."""
    return a + b

def rectangle_area(a, b):
    """Площа прямокутника."""
    return a * b

def is_prime(num):
    """Перевіряє, чи є число простим."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Приклади викликів
a = float(input("Введіть перше число для суми: "))
b = float(input("Введіть друге число для суми: "))
print("Сума:", add_numbers(a, b))

x = float(input("Сторона a прямокутника: "))
y = float(input("Сторона b прямокутника: "))
print("Площа прямокутника:", rectangle_area(x, y))

n = int(input("Введіть число для перевірки на простоту: "))
print(f"{n} є простим:", is_prime(n))
