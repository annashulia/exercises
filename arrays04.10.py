import array

arr1 = array.array('i', [5, 3, 8, 1, 2])
arr2 = array.array('i', [4, 5, 6, 7, 8])

arr1.append(4)
arr2.extend([9, 10, 11])

print("After arr1.append(4), arr1 is:", arr1)
print(arr2)


index = 3
removed = arr2.pop(index)

arr2.remove(5)

print("Removed from arr2 at index", index, ":", removed)
print("arr2 now:", list(arr2))
print("arr2 after remove(5):", list(arr2))

arr1 = array.array('i', sorted(arr1))
arr2 = array.array('i', sorted(arr2))
print("arr1 sorted:", list(arr1))
print("arr2 sorted:", list(arr2))




