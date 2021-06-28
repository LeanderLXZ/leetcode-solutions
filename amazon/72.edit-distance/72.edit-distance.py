#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (47.75%)
# Likes:    5936
# Dislikes: 70
# Total Accepted:    368.1K
# Total Submissions: 769.1K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
# 
# Constraints:
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    
    # Dynamic Programming
    # Time complexity : O(mn)
    # as it follows quite straightforward for the inserted loops.
    # Space complexity : O(mn)
    # since at each step we keep the results of all previous computations.
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if not m or not n:
            return m + n
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(dp[i][j]-1, dp[i+1][j], dp[i][j+1]) + 1
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        return dp[-1][-1]
        
# @lc code=end

