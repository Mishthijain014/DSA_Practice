nums = [1,1,2,2,3]

slow = 0

for fast in range(1,len(nums)):
    if nums[slow]!=nums[fast]:
        slow += 1
        nums[slow] = nums[fast]

print(nums)