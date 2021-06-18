#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (56.03%)
# Likes:    3207
# Dislikes: 2572
# Total Accepted:    698.1K
# Total Submissions: 1.2M
# Testcase Example:  '[3,0,1]'
#
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.
# 
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
# [0,3]. 2 is the missing number in the range since it does not appear in
# nums.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range
# [0,2]. 2 is the missing number in the range since it does not appear in
# nums.
# 
# 
# Example 3:
# 
# 
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range
# [0,9]. 8 is the missing number in the range since it does not appear in
# nums.
# 
# 
# Example 4:
# 
# 
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range
# [0,1]. 1 is the missing number in the range since it does not appear in
# nums.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    
    # XOR
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    
    # Gauss' Formula
    # def missingNumber(self, nums: List[int]) -> int:
    #     p = 0
    #     for n in nums:
    #         p += n
    #     return len(nums) * (len(nums) + 1) // 2 - p
    
    # Gauss' Formula
    # def missingNumber(self, nums):
    #     expected_sum = len(nums)*(len(nums)+1)//2
    #     actual_sum = sum(nums)
    #     return expected_sum - actual_sum
    
    # Gauss' Formula
    # def missingNumber(self, nums: List[int]) -> int:
    #     p = 0
    #     s = 0
    #     for i, n in enumerate(nums):
    #         p += n
    #         s += i + 1
    #     return s - p
        
# @lc code=end

