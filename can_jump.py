def can_jump(nums):
    goal = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] + i >= goal:
            goal = i
    return True if goal == 0 else False

nums = [2, 3, 4, 0, 1]

print(can_jump(nums))