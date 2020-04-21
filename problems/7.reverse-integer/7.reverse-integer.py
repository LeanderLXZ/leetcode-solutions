#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.65%)
# Likes:    3068
# Dislikes: 4837
# Total Accepted:    1M
# Total Submissions: 4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    
    def reverse(self, x: int) -> int:
        int_max = 2**31 - 1
        x_abs = abs(x)
        num_list = []
        x_reversed = 0
        while x_abs != 0:
            x_abs, c = divmod(x_abs, 10)
            x_reversed = x_reversed * 10 + c
            if x_reversed > 2**31 - 1:
                return 0
        if x < 0:
            return x_reversed * -1
        else:
            return x_reversed
        
# @lc code=end

