#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (61.91%)
# Likes:    5356
# Dislikes: 355
# Total Accepted:    609.6K
# Total Submissions: 984.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: [[1]]
# 
# 
# Example 4:
# 
# 
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
# 
# 
# 
# Constraints:
# 
# 
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    
    # Rotate Groups of Four Cells
    # Time complexity : O(M), as each cell is getting read once and written once.
    # Space complexity : O(1) because we do not use any other additional data structures.
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     n = len(matrix[0])
    #     for i in range(n // 2 + n % 2):
    #         for j in range(n // 2):
    #             tmp = matrix[n - 1 - j][i]
    #             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
    #             matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
    #             matrix[j][n - 1 - i] = matrix[i][j]
    #             matrix[i][j] = tmp
    
    # Reverse on Diagonal and then Reverse Left to Right
    # Time complexity : O(M). 
    # We perform two steps; transposing the matrix, and then reversing each row. 
    # Transposing the matrix has a cost of O(M) because we're moving the value 
    # of each cell once. Reversing each row also has a cost of O(M), because 
    # again we're moving the value of each cell once.
    
    # Space complexity : O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(n):
            for j in range(n//2):
                matrix[i][-j-1], matrix[i][j] = matrix[i][j], matrix[i][-j-1]
        
# @lc code=end

