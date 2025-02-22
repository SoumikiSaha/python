def mergeSort(arr, n):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = mergeSort(left_half, len(left_half))
    right_sorted = mergeSort(right_half, len(right_half))

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare elements and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left and right halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
print(mergeSort(arr, len(arr)))