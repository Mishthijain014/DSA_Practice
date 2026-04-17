# nums = [1, 2, 2]   
# result = []

# nums.sort()

# def backtrack(index, subset):
#     result.append(subset[:])

#     for i in range(index, len(nums)):
#         if i > index and nums[i] == nums[i - 1]:
#             continue

#         subset.append(nums[i])
#         backtrack(i + 1, subset)
#         subset.pop()


# backtrack(0, [])
# print(result)


result = []
nums = [1,1,2]

def backtracking(index,subsets):
    result.append(subsets[:])

    for i in range(index,len(nums)):
        if i>index and nums[i]==nums[i-1]:
            continue

        subsets.append(nums[i])
        backtracking(i+1,subsets)

        subsets.pop()

backtracking(0,[])
print(result)