#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (34.07%)
# Likes:    4340
# Dislikes: 424
# Total Accepted:    662.3K
# Total Submissions: 1.9M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int):
        if nums == []:
            return -1
        self.target = target
        return self.binary_search(nums, 0)
        
    def binary_search(self, nums, i):
        if nums[0] == self.target:
            return i
        i_middle = len(nums) // 2
        num_first = nums[0]
        num_middle = nums[i_middle]
        if num_first < num_middle:
            if num_first <= self.target < num_middle:
                return self.binary_search(nums[:i_middle], i)
            else:
                return self.binary_search(nums[i_middle:], i+i_middle)
        elif num_middle < num_first:
            if num_middle <= self.target < num_first:
                return self.binary_search(nums[i_middle:], i+i_middle)
            else:
                return self.binary_search(nums[:i_middle], i)
        else:
            return -1
            
# @lc code=end

