#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.82%)
# Likes:    8410
# Dislikes: 509
# Total Accepted:    1.4M
# Total Submissions: 4.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         len_sub = 0
#         sub = []
#         for i in s:
#             if i in sub:
#                 sub = sub[sub.index(i)+1:]
#             sub.append(i)
#             len_sub = max(len_sub, len(sub))
#         return len_sub


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1:
            # return 1
        len_sub = 0
        sub_dict = {}
        left_index = 0
        for i, s_i in enumerate(s):
            if s_i in sub_dict:
                if sub_dict[s_i] >= left_index:
                    left_index = sub_dict[s_i] + 1
            sub_dict[s_i] = i
            len_sub = max(len_sub, i - left_index + 1)
        return len_sub
        
# @lc code=end

