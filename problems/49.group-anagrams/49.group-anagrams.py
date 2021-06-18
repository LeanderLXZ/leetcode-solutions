#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (60.44%)
# Likes:    5731
# Dislikes: 239
# Total Accepted:    950K
# Total Submissions: 1.6M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.
# 
# 
#

# @lc code=start
class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = {}
    #     for s in strs:
    #         s_sorted = tuple(sorted(s))
    #         if s_sorted in res:
    #             res[s_sorted].append(s)
    #         else:
    #             res[s_sorted] = [s]
    #     return list(res.values())
    
    # Categorize by Sorted String
    # Time Complexity: O(NKlogK), where NN is the length of strs, and KK is the
    # maximum length of a string in strs. The outer loop has complexity O(N)
    # as we iterate through each string. Then, we sort each string in O(KlogK) time.
    # Space Complexity: O(NK), the total information content stored in ans.
    # def groupAnagrams(self, strs):
    #     ans = collections.defaultdict(list)
    #     for s in strs:
    #         ans[tuple(sorted(s))].append(s)
    #     return ans.values()
    
    # Categorize by Count - No sorting
    # Time Complexity: O(NK), where NN is the length of strs, and KK is the 
    # maximum length of a string in strs. Counting each string is linear in the
    # size of the string, and we count every string.
    # Space Complexity: O(NK), the total information content stored in ans.
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
        
# @lc code=end

