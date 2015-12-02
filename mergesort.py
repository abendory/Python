def mergesort(s):
    if len(s) > 1:
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i += 1
            else:
                s[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            s[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            s[k] = right[j]
            j += 1
            k += 1

import random
array = []
for i in range(20):
    array.append(random.randint(1, 9))

print("Unsorted array: ", array)
mergesort(array)
print("Sorted array:   ", array)