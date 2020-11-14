#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (72.25%)
# Likes:    1620
# Dislikes: 103
# Total Accepted:    334.4K
# Total Submissions: 463.9K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.
#
#
#
#
# Example 1:
#
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
#
#
# Example 2:
#
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
#
#
#
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        out = []
        left = 0
        right = len(A) - 1
        while left <= right:
            if abs(A[left]) < abs(A[right]):
                out.append(A[right] ** 2)
                right -= 1
            else:
                out.append(A[left] ** 2)
                left += 1
        return out[::-1]
        
# @lc code=end

