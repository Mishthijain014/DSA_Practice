nums = [1,1,3]
result = []
path = []
visited = [False]*len(nums)
nums.sort()


def backtrack():
    if(len(path)==len(nums)):
        result.append(path[:])
        return

    for i in range(len(nums)):
        if visited[i]:
            continue

        if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
            continue

        path.append(nums[i])
        visited[i] = True

        backtrack()

        path.pop()
        visited[i] = False

        
backtrack()
print(result)