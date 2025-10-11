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


def bubble_sort_with_swaps(a: array.array):
    for n in range(len(a) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                print(list(a))
        if not swapped:
            break

print("Start:", list(arr1))
bubble_sort_with_swaps(arr1)
print("Sorted array is:")
print(list(arr1))


