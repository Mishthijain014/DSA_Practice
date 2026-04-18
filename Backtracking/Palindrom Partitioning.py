s = "aab"
result = []
def partition(s):

    def is_palindrom(sub):
        return sub == sub[::-1]
    
    def backtracking(start,path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start,len(s)):
            substring = s[start:end+1]

            if is_palindrom(substring):
                path.append(substring)
                backtracking(end+1,path)
                path.pop()

    backtracking(0,[])
    return result

print(partition(s))



