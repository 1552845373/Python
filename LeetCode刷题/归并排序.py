#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/10/31 10:21
# @Author : Cheng
# @File : 归并排序.py
# @Software : PyCharm

from typing import List

class Solution:
    def __init__(self) -> None:
        self.count = 0

    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.count

    def mergeSort(self, nums):
        if len(nums) <= 1: return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        l, r = 0, 0
        li = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                li.append(left[l])
                l += 1
            else:
                li.append(right[r])
                r += 1
                self.count += len(left) - l
        li += left[l:]
        li += right[r:]
        return li

if __name__ == "__main__":
    mylist = [12, 33, 199, 0, 54, 33, 11]
    result = Solution().mergeSort(mylist)
    print(f'归并排序后：{result}')