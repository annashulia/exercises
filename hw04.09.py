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

min = list[0]
max = list[0]

for i in range (len(list)):
   if list[i] > max:
     max = list[i]
   elif list[i] < min:
     min = list[i]
      
print("Min:", min)
print("Max:", max)

#Count the number of even and odd elements

even_count = 0
odd_count = 0
for number in list:
     if number % 2 == 0:
         even_count += 1
     elif number % 2 == 1:
         odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

#Count the number of positive, negative and zero elements

positive_count = 0
negative_count = 0
zero_count = 0
for number in list:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else: 
        zero_count += 1

print("Positives:", positive_count)
print('Negatives:', negative_count) 
print("Zeros:", zero_count) 