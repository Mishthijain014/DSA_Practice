nums = [3,2,4]
target = 6

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
            break
        
# In this ques you can not use two pointer method as this method only works on sorted array