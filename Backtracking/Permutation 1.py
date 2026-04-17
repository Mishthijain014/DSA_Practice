nums = [1,2,3]
result = []
path = []
visited = [False]*len(nums)

def backtrack():
    if(len(path)==len(nums)):
        result.append(path[:])
        return
            
    for i in range(len(nums)):
        if visited[i]:
            continue

        path.append(nums[i])
        visited[i] = True

        backtrack()

        path.pop()
        visited[i] = False

backtrack()
print(result)
