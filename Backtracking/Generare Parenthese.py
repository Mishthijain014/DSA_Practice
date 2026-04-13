n = 3
result = []

def backtracking(curr,open,close):
    if(len(curr)==n*2):
        result.append(curr)
        return
    
    if open<n:
        backtracking(curr + "(" , open+1,close)

    if close<open:
        backtracking(curr + ")" , open,close+1)

backtracking("",0,0)
print(result)