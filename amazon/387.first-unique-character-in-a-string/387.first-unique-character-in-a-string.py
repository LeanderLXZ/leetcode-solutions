#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (54.46%)
# Likes:    3111
# Dislikes: 150
# Total Accepted:    761.6K
# Total Submissions: 1.4M
# Testcase Example:  '"leetcode"'
#
# Given a string s, return the first non-repeating character in it and return
# its index. If it does not exist, return -1.
# 
# 
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
    
    # def firstUniqChar(self, s: str) -> int:
    #     seen = {}
    #     for i, c in enumerate(s):
    #         if c in seen:
    #             seen[c][0] = i
    #             seen[c][1] += 1
    #         else:
    #             seen[c] = [i, 1]
    #     for i, v in seen.values():
    #         if v == 1:
    #             return i
    #     return -1
        
# @lc code=end

