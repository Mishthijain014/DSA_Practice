Candidates= [10,1,2,7,6,1,5]
target = 8
result = []

Candidates.sort()

def backtracking(index,target,path):
    if target == 0:
        result.append(path[:])
        return
    
    if target <0:
        return
    
    for i in range(index,len(Candidates)):
        if i>index and Candidates[i]==Candidates[i-1]:
            continue

        path.append(Candidates[i])

        backtracking(i+1,target - Candidates[i],path)

        path.pop()

backtracking(0,target,[])
print(result)