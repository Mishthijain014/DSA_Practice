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
      
