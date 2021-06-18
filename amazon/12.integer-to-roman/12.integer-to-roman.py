#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (57.52%)
# Likes:    1849
# Dislikes: 3223
# Total Accepted:    502.7K
# Total Submissions: 873.9K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given an integer, convert it to a roman numeral.
# 
# 
# Example 1:
# 
# 
# Input: num = 3
# Output: "III"
# 
# 
# Example 2:
# 
# 
# Input: num = 4
# Output: "IV"
# 
# 
# Example 3:
# 
# 
# Input: num = 9
# Output: "IX"
# 
# 
# Example 4:
# 
# 
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 3999
# 
# 
#

# @lc code=start
class Solution:
    
    # Time complexity : O(1).
    # The same number of operations is done, regardless of the size of the 
    # input. Therefore, the time complexity is constant.
    
    # Space complexity : O(1).
    # While we have Arrays, they are the same size, regardless of the size of 
    # the input. Therefore, they are constant for the purpose of 
    # space-complexity analysis.
    def intToRoman(self, num: int) -> str:
        roman_1 = ['', 'M', 'MM', 'MMM']
        roman_2 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        roman_3 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        roman_4 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return roman_1[num // 1000] + roman_2[num % 1000 // 100] + roman_3[num % 100 // 10] + roman_4[num % 10]

# @lc code=end

