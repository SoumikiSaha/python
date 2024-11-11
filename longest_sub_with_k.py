def longestSubarrayWithSumK(a, k):
    # Write your code here
    start = 0
    current_sum = 0
    max_length = 0
    n = len(a)
    
    for end in range(n):
        current_sum += a[end]
        
        # Shrink the window from the left if the current_sum exceeds k
        while current_sum > k and start <= end:
            current_sum -= a[start]
            start += 1
        
        # Check if the current_sum is equal to k
        if current_sum == k:
            max_length = max(max_length, end - start + 1)
    
    return max_length



