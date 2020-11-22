#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (57.44%)
# Likes:    4568
# Dislikes: 144
# Total Accepted:    971.3K
# Total Submissions: 1.7M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
#

# @lc code=start
class Solution:
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = []
        for i in range(len(nums)):
            if nums[i] == 0:
                queue.append(i)
            elif queue:
                if i > queue[0]:
                    i_zero = queue.pop(0)
                    nums[i_zero], nums[i] = nums[i], 0
                    queue.append(i)
        return nums
    
    # Space Complexity : O(1). Only constant space is used.
    # Time Complexity: O(n). However, the total number of operations are optimal. 
    def moveZeroes(self, nums: List[int]) -> None:
        i_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[i_zero] = nums[i_zero], nums[i]
                i_zero += 1
        return nums
        
        
# @lc code=end

