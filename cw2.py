'''
Variables
Task:
Create two variables: a = 5 and b = 10.
Swap their values (so that a becomes 10, and b becomes 5) without creating a new variable.

Hint: you can use simultaneous assignment.
'''

a = 5
b = 10

# swapping values
a, b = b, a

print(a)  # 10
print(b)  # 5
