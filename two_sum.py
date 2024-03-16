list_nums = [[1, 2, 3, 4, 5], [5, 0, 2, 1, 99, 4], [1, 1, 1, 3, 0, 0, 8]]
target = 9
def two_sum(nums, target):
    index_list = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                index_list.append(i)
                index_list.append(j)
    return index_list
for l in list_nums:
    value = two_sum(l, target)
    print(value)