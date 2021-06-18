#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (56.12%)
# Likes:    2822
# Dislikes: 743
# Total Accepted:    589K
# Total Submissions: 1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers numbers that is already sorted in non-decreasing
# order, find two numbers such that they add up to a specific target number.
# 
# Return the indices of the two numbers (1-indexed) as an integer array answer
# of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# 
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
# 
# 
# Example 1:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
# 
# Example 2:
# 
# 
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# 
# 
# Example 3:
# 
# 
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
# 
# 
#

# @lc code=start
class Solution:
    
    # Two pointers to variables
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return left+1, right+1
            elif sum < target:
                left += 1
            else:
                right -= 1
    
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     dict_diff = {}
    #     for i, n in enumerate(numbers):
    #         if n in dict_diff:
    #             return dict_diff[n]+1, i+1
    #         else:
    #             dict_diff[target - n] = i
        
# @lc code=end

