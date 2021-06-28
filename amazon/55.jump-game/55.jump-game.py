#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (35.57%)
# Likes:    6794
# Dislikes: 437
# Total Accepted:    660.5K
# Total Submissions: 1.9M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    
    # Greedy
    # Time complexity : O(n)
    # Space complexity : O(1)
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if (i + nums[i] >= last):
                last = i
        return last == 0
    
    # Greedy
    # Time complexity : O(n)
    # Space complexity : O(1)
    # def canJump(self, nums: List[int]) -> bool:
    #     destination = len(nums)-1
    #     source = destination-1
    #     while source >= 0:
    #         if source + nums[source] >= destination:
    #             destination = source
    #         source-=1
    #     return destination == 0
    
    # Dynamic Programming - Time Limit Exceeded
    # Time complexity : O(n^2)
    # Space complexity : O(n)
    # def canJump(self, nums: List[int]) -> bool:
    #     dp = [False] * len(nums)
    #     dp[0] = True
    #     for i in range(1, len(nums)):
    #         for j in range(i):
    #             if dp[j] and nums[j] + j >= i:
    #                 dp[i] = True
    #                 break
    #         if not dp[i]:
    #             break
    #     return dp[-1]
    
    
        
# @lc code=end

