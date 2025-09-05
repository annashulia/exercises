# Find amount of elements in the list using loop
list = [1, 4, 7, -9]
total = 0 

for element in list:
    total += 1    
    

print("Number of elements:", total) 

#Find product of elements in the list

update = 1
for i in list:
    update *= i 

print(update)


#Find min and max from elements in the list

min_val = list[0]
max_val = list[0]

for num in list:
    if num > max_val:
        max_val = num
    elif num < min_val:
        min_val = num
print("Min:", min)
print("Max:", max)

#Count the number of even and odd elements

parity_counts = [0, 0]   # odd, even values
for num in list:
    if num % 2 == 0:
        parity_counts[0] += 1
    else:
        parity_counts[1] += 1
print("Even numbers:", parity_counts[0])
print("Odd numbers:", parity_counts[1])

#Count the number of positive, negative and zero elements

sign_counts = [0, 0, 0]  #positive, negative and zero elements
for num in list:
    if num > 0:
        sign_counts[0] += 1
    elif num < 0:
        sign_counts[1] += 1
    else:
        sign_counts[2] += 1
print("Positives:", sign_counts[0])
print("Negatives:", sign_counts[1])
print("Zeros:", sign_counts[2])
