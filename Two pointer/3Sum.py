# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         result = []
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if nums[i]+nums[j]+nums[k] == 0:
#                         triplet = sorted([nums[i],nums[j],nums[k]])
#                         if triplet not in result:
#                             result.append(triplet)

#         return result
        
