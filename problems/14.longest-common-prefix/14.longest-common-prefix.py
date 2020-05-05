#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.88%)
# Likes:    2232
# Dislikes: 1741
# Total Accepted:    688.7K
# Total Submissions: 2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        # if strs == []:
        #     return ''
        # prefix = strs[0]
        # for word in strs[1:]:
        #     max_len = min(len(word), len(prefix))
        #     prefix = prefix[:max_len]
        #     for i, c in enumerate(word[:max_len]):
        #         if c != prefix[i]:
        #             prefix = prefix[:i]
        #             if not prefix:
        #                 return ''
        #             break
        # return prefix

        if strs == []:
            return ''
        i = 0
        while True:
            try:
                c = strs[0][i]
                for word in strs:
                    if c != word [i]:
                        return word[:i]
            except IndexError:
                return strs[0][:i]
            i += 1
        
# @lc code=end

