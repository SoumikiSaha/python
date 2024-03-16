nums = [-1,0,1,2,-1,-4]
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    triplets = []
    nums.sort()
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k] == 0) and (i != j and i != k and j != k) and [nums[i], nums[j], nums[k]] not in triplets:
                    triplets.append([nums[i], nums[j], nums[k]])
    return triplets
value = threeSum(nums)
print(value)