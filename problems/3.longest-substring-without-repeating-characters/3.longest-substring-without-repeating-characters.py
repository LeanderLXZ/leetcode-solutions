#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
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

