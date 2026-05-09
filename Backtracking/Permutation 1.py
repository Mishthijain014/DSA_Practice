nums = [1,2,3]
result = []
path = []
visited = [False]*len(nums)

def backtracking():
    if(len(path)==len(nums)):
        result.append(path[:])
        return
    
    for i in range(len(nums)):
        if visited[i] == True:
            continue

        path.append(nums[i])
        visited[i] = True

        backtracking()

        path.pop()
        visited[i] = False

backtracking()
print(result)



