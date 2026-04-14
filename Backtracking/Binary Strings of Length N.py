n = 3
result = []

def backtracking(index,path):
    if n==len(path):
        result.append(path[:])
        return
    
    backtracking(index+1,path+'0')
    backtracking(index+1,path+'1')

backtracking(0,"")
print(result)