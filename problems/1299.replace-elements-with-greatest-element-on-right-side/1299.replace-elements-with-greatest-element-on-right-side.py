#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
#
# algorithms
# Easy (76.61%)
# Likes:    538
# Dislikes: 125
# Total Accepted:    88.7K
# Total Submissions: 119K
# Testcase Example:  '[17,18,5,4,6,1]'
#
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with
# -1.
#
# After doing so, return the array.
#
#
# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5
#
#

# @lc code=start
class Solution:
           
    # Left to right
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_a = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                if arr[i] >= max_a:
                    max_a = 0
                    for j in range(i + 1, len(arr)):
                        max_a = max(arr[j], max_a)
                arr[i] = max_a
        return arr
    
    # Right to left
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_a = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], max_a = max_a, max(arr[i], max_a)
        return arr

# @lc code=end

