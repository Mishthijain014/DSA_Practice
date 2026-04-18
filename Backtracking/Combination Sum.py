candidates = [2,3,6,7]
target = 7
result = []

def baktracking(index,target,path):
    if target == 0:
        result.append(path[:])
        return
    
    if target<0:
        return
    
    for i in range(index,len(candidates)):
        path.append(candidates[i])

        baktracking(i,target-candidates[i],path)

        path.pop()

baktracking(0,target,[])
print(result)
