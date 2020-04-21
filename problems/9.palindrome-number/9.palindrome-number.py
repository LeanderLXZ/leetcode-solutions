#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (47.22%)
# Likes:    2092
# Dislikes: 1505
# Total Accepted:    860.8K
# Total Submissions: 1.8M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Could you solve it without converting the integer to a string?
# 
#

# @lc code=start
from math import floor, log
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x > 0:
            n_bit = floor(log(x, 10)) + 1
            for i in range(1, n_bit // 2 + 1):
                x, bit_right = divmod(x, 10)
                bit_left = x // 10**(n_bit - 2 * i) % 10
                print(bit_left, bit_right)
                if bit_left != bit_right:
                    return False
            return True
        else:
            return False
        
# @lc code=end

