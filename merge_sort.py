from math import ceil
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_arr = []
mid = ceil(len(arr)/2)
left_arr = []
for i in range(0, mid):
    left_arr.append(arr[i])

right_arr = []
for j in range(mid, len(arr)):
    right_arr.append(arr[j])

# for l in range(0, len(left_arr)):
#     for r in range(0, len(right_arr)):
#         if left_arr[l] < right_arr(r):
