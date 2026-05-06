def max_num_of_k_pair(nums,k):
    nums.sort()

    left = 0
    right = len(nums)-1
    count = 0

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == k:
            count += 1
            right -= 1
            left += 1

        if curr_sum < k:
            left += 1

        else:
            right -= 1

    return count 

print(max_num_of_k_pair([1,2,3],5))