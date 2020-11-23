#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (51.43%)
# Likes:    1950
# Dislikes: 122
# Total Accepted:    431.1K
# Total Submissions: 800.9K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#

# @lc code=start
class Solution:
    
    # Time complexity: O(numRows^2)
    # Space complexity : O(numRows^2)
    def generate(self, numRows: int) -> List[List[int]]:
        out_list = [[1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return out_list
        for _ in range(numRows - 1):
            out = [1]
            pre_list = out_list[-1]
            for i in range(len(pre_list)-1):
                out.append(pre_list[i] + pre_list[i+1])
            out_list.append(out + [1])
        return out_list
    
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        pre_list = self.generate(numRows- 1)
        pre_row, out = pre_list[-1], [1]
        for i in range(len(pre_row)-1):
            out.append(pre_row[i] + pre_row[i+1])
        return pre_list + [out + [1]]
        
# @lc code=end

