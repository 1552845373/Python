#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/9/7 14:14
# @Author : Cheng
# @File : 调试.py
# @Software : PyCharm

# def nextGreaterElement(nums1, nums2):
#     List = []
#     n = len(nums2)
#     for i in nums1:
#         index = nums2.index(i)
#         for j in range(index, n):
#             if nums2[j] > i:
#                 List.append(nums2[j])
#                 break
#             if j == n-1:
#                 List.append(-1)
#     return List
#
# if __name__ == '__main__':
#     nums1 = [4, 1, 2]
#     nums2 = [1, 3, 4, 2]
#     print(nextGreaterElement(nums1=nums1,nums2=nums2))

# class Solution:
#     def reverseString(self, s):
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         if len(s)<=1:
#             return s
#         out = self.reverseString(s[1:]) + [s[0]]
#         return out
#
# if __name__ == '__main__':
#     print(Solution().reverseString(["H","a","n","n","a","h"]))

from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

print(Solution().majorityElement([3,2,3]))

