#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/9/7 14:14
# @Author : Cheng
# @File : 调试.py
# @Software : PyCharm

from typing import List
import copy

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         ans = []
#         def backtrack(S, left, right):
#             if len(S) == 2 * n:
#                 ans.append(''.join(S))
#                 return
#             if left < n:
#                 S.append('(')
#                 backtrack(S, left+1, right)
#                 S.pop()
#             if right < left:
#                 S.append(')')
#                 backtrack(S, left, right+1)
#                 S.pop()
#
#         backtrack([], 0, 0)
#         return ans
#
# if __name__ == '__main__':
#     Solution().generateParenthesis(3)

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l = len(nums)
#         nums1 = copy.deepcopy(nums)
#         for i in range(l):
#             nums1[(i+k)%l] = nums[i]
#         nums = copy.deepcopy(nums1)
#         return nums
#
# if __name__ == '__main__':
#     print(Solution().rotate([1,2,3,4,5,6,7],3))

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key=lambda x:x[0])
#         count = 0
#         for i in range(len(intervals)-1):
#             i -= count
#             if intervals[i][1]>=intervals[i+1][0]:
#                 if intervals[i][1] >= intervals[i+1][1]:
#                     intervals.pop(i+1)
#                 else:
#                     intervals.insert(i,[intervals.pop(i)[0],intervals.pop(i)[1]])
#                 count += 1
#         return intervals
#
# if __name__ == '__main__':
#     print(Solution().merge([[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]))

def insert_sort(nums):
    n = len(nums)
    for i in range(1,n):
        j = i
        tmp = nums[i]
        while j>0 and nums[j]<nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j-1] = tmp
    return nums