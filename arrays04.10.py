import array

arr1 = array.array('i', [5, 3, 8, 1, 2])
arr2 = array.array('i', [4, 5, 6, 7, 8])

arr1.append(4)
arr2.extend([9, 10, 11])

print("After adding 4 to arr1:", list(arr1))
print("After adding elements to arr2:", list(arr2))


index = 3
removed = arr1.pop(index)

arr2.remove(5)

print("Removed 1 from arr1 using index", list(arr1))
print("arr2 after removing 5:", list(arr2))



def bubble_sorted(a: array.array) -> array.array:
    b = array.array(a.typecode, a)  
    n = len(b)
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                swapped = True
        if not swapped:
            break
    return b

arr = array.array('i', [5, 3, 8, 1, 2])
print("Original:", list(arr))
sorted_arr = bubble_sorted(arr)
print("Sorted (bubble):", list(sorted_arr))

