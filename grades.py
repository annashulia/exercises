import random

grades = []

for i in range(5):
    grade = random.randint(1, 12)
    grades.append(grade)

total_sum = 0
count = 0

for grade in grades:
    total_sum += grade
    count += 1

average_grade = total_sum / count

print("Grade values:", grades)

print(f"Average: ({total_sum}) / {count} = {average_grade}")

