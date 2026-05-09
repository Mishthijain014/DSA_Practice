nums = [2, 2, 2]   
result = []

nums.sort()

def backtracking(index,subset):
    result.append(subset[:])

    for i in range(index,len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue

        subset.append(nums[index])
        backtracking(index+1,subset)
        subset.pop()

backtracking(0,[])
print(result)
