n = 4
k = 2

result = []

def backtracking(index,path):
    if(k==len(path)):
        result.append(path[:])
        return

    for i in range(index,n-(k-len(path))+2):
        path.append(i)
        backtracking(i+1,path)
        path.pop()
        
backtracking(1,[])
print(result)