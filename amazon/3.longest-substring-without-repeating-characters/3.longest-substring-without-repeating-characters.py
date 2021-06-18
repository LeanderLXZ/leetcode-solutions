#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.80%)
# Likes:    15042
# Dislikes: 766
# Total Accepted:    2.3M
# Total Submissions: 7.1M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# Example 4:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    
    # Time O(n)
    # Space O(m)
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_ch = {}
        res = 0
        left = 0
        for right in range(len(s)):
            if s[right] in dict_ch:
                # Be careful! left pointer should not go back
                left = max(dict_ch[s[right]] + 1, left)
            dict_ch[s[right]] = right
            res = max(res, right - left + 1)
        return res
                
                
        
# @lc code=end

