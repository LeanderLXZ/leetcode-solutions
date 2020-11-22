#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (34.30%)
# Likes:    548
# Dislikes: 81
# Total Accepted:    94.2K
# Total Submissions: 291.6K
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < A[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
        
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        while i < len(arr) - 1:
            if arr[i] <= arr[i-1]:
                break
            i += 1
        if i == 1:
            return False
        while i < len(arr):
            if arr[i] >= arr[i-1]:
                return False
            i += 1
        return True
    
    # Time Complexity: O(N), where N is the length of arr.
    # Space Complexity: O(1)
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0
        while i < N - 1 and arr[i] < arr[i+1]:
            i += 1
        if i == 0 or i == N - 1:
            return False
        while i < N - 1 and arr[i] > arr[i+1]:
            i+= 1
        return i == N - 1
        
# @lc code=end

