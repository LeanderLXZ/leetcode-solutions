#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (48.17%)
# Likes:    1135
# Dislikes: 212
# Total Accepted:    338.7K
# Total Submissions: 658.3K
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th row of the Pascal's
# triangle.
#
# Notice that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#
# Constraints:
#
#
# 0 <= rowIndex <= 40
#
#
#

# @lc code=start
class Solution:
    
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        pre_row, out = self.getRow(rowIndex - 1), [1]
        for i in range(len(pre_row)-1):
            out.append(pre_row[i] + pre_row[i+1])
        return out + [1]
    
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        out_list = [1]
        for _ in range(rowIndex):
            out = [1]
            for i in range(len(out_list)-1):
                out.append(out_list[i] +out_list[i+1])
            out_list = out + [1]
        return out_list
        
# @lc code=end

