#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium
# Testcase Example:  '[1,0,1,1,0,1]\n2'
#
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0. 
#
#
#
#
# Example 1:
#
#
# Input: A = [1,0,1,1,0]
# Output: 4
# Explanation:
# Flip the first zero will get the the maximum number of consecutive 1s.
# After flipping, the maximum number of consecutive 1s is 4.
#
#
#
#
# Note:
#
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#
#

# @lc code=start
class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre, cur, out = -1, 0, 0
        for i in nums:
            if i == 0:
                pre, cur = cur, 0
            else:
                cur += 1
            out = max(out, pre + cur + 1)
        return out
        
# @lc code=end

