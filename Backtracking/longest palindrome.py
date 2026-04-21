# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         result = ""
#         def is_palindrome(sub):
#             return sub == sub[::-1]

#         def backtracking(start,path):
#             nonlocal result

#             for end in range(start,len(s)):
#                 substring = s[start:end+1]

#                 if is_palindrome(substring):
#                     path.append(substring)
#                     backtracking(end+1,path)
#                     path.pop()

#             if path:
#                 last = path[-1]
#                 if len(last)>len(result):
#                     result = last             

#         backtracking(0,[])
#         return result

s = "babad"
res =""

def expand(left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

for i in range(len(s)):
    temp1 = expand(i,i)
    temp2 = expand(i,i+1)

    if len(temp1) > len(res):
        res = temp1
    if len(temp2) > len(res):
        res = temp2

print(res)   
