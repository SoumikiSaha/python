def find_product(nums):
    answer = []
    for n in range(len(nums)):
        new_list = [nums[_f] for _f in range(len(nums)) if _f != n]
        product = 1
        for num in new_list:
            product *= num
        answer.append(product) 
    return answer

nums = [1,2,4,6]
print(find_product(nums))

