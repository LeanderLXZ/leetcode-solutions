#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.31%)
# Likes:    8986
# Dislikes: 251
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#

# @lc code=start
class Solution:
    
    # dfs
    # Time complexity : O(M×N)
    # where M is the number of rows and N is the number of columns.
    # Space complexity : worst case O(M×N)
    # in case that the grid map is filled with lands where DFS goes by M×N deep.
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
    
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        queue = [(i, j)]
        while queue:
            cur_i, cur_j = queue.pop()
            if grid[cur_i][cur_j] == '1':
                grid[cur_i][cur_j] = '0'
                queue.extend([
                    (max(cur_i-1, 0), cur_j),
                    (min(cur_i+1, m-1), cur_j),
                    (cur_i, max(cur_j-1, 0)),
                    (cur_i, min(cur_j+1, n-1)),
                ])
        
# @lc code=end

