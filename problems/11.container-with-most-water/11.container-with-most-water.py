#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (53.04%)
# Likes:    9891
# Dislikes: 732
# Total Accepted:    977.1K
# Total Submissions: 1.8M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: height = [4,3,2,1,4]
# Output: 16
# 
# 
# Example 4:
# 
# 
# Input: height = [1,2,1]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:

    # Time complexity : O(n). Single pass.
    # Space complexity : O(1). Constant space is used.
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            h_left = height[left]
            h_right = height[right]
            area = max(area, min(h_left, h_right) * (right - left))
            if h_left < h_right:
                left = left + 1
            else:
                right = right - 1
        return area
            
        
# @lc code=end

