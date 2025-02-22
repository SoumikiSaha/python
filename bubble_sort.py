def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                (arr[i], arr[j]) = (arr[j], arr[i])
    return arr

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
print(bubble_sort(arr))