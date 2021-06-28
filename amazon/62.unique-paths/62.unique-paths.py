#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (56.89%)
# Likes:    5488
# Dislikes: 249
# Total Accepted:    667.4K
# Total Submissions: 1.2M
# Testcase Example:  '3\n7'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Example 1:
# 
# 
# Input: m = 3, n = 7
# Output: 28
# 
# 
# Example 2:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# 
# Example 3:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
# 
# Example 4:
# 
# 
# Input: m = 3, n = 3
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.
# 
# 
#

# @lc code=start
class Solution:
    
    # Dynamic Programming
    # Time complexity: O(N×M).
    # Space complexity: O(N×M).
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m ):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
    # Math
    # Time complexity: O((M+N)(log(M+N)loglog(M+N))^2)
    # Space complexity: O(1)
    # def uniquePaths(self, m: int, n: int) -> int:
    #     return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
        
# @lc code=end

