#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (30.34%)
# Likes:    812
# Dislikes: 1454
# Total Accepted:    183K
# Total Submissions: 599K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
#
# Example 1:
#
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
#
#
#
# Example 2:
#
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
#
#
#
# Example 3:
#
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#
#

# @lc code=start
class Solution:
    
    def thirdMax(self, nums: List[int]) -> int:
        stack = [nums[0]]
        for n in nums[1:]:
            if n not in stack:
                if len(stack) < 3:
                    stack.append(n)
                elif n > min(stack):
                    stack.pop(stack.index(min(stack)))
                    stack.append(n)
                else:
                    pass
        if len(stack) < 3:
            return max(stack)
        return min(stack)
    
    # Using sets
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def thirdMax(self, nums: List[int]) -> int:
        mx = set()
        for n in nums:
            mx.add(n)
            if len(mx) > 3:
                mx.remove(min(mx))
        if len(mx) == 3:
            return min(mx)
        return max(mx)

        
# @lc code=end

