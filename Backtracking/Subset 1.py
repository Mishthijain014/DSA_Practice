result =[]
nums = [1,2,3]

def backtracking(index,subset):
    if(index==len(nums)):
        result.append(subset[:])
        return 
    
    subset.append(nums[index])
    backtracking(index+1,subset)

    subset.pop()
    backtracking(index+1,subset)


backtracking(0,[])
print(result)

