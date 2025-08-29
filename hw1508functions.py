def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def rectangle_area(a, b):
    """Calculates the area of a rectangle."""
    return a * b

def is_prime(num):
    """Checks whether a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example calls
a = float(input("Enter the first number to add: "))
b = float(input("Enter the second number to add: "))
print("Sum:", add_numbers(a, b))

x = float(input("Side a of the rectangle: "))
y = float(input("Side b of the rectangle: "))
print("Area of the rectangle:", rectangle_area(x, y))

n = int(input("Enter a number to check for primality: "))
print(f"{n} is prime:", is_prime(n))
