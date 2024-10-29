def twoSum(nums, target):
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

arr = [0, 3, 4, 5, 6, 2]
answer = twoSum(arr, 2)
print(answer)