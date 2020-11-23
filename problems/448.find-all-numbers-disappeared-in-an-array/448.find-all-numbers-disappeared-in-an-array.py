#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (55.63%)
# Likes:    3496
# Dislikes: 270
# Total Accepted:    311.2K
# Total Submissions: 555.3K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
#
#
#

# @lc code=start
class Solution:
        
    # Time Complexity : O(N)
    # Space Complexity : O(N)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map_n = {n:1 for n in nums}
        out = []
        for i in range(1, len(nums) + 1):
            if i not in map_n:
                out.append(i)
        return out
    
    # Time Complexity : O(N)
    # Space Complexity : O(1) since we are reusing the input array itself as a
    # hash table and the space occupied by the output array doesn't count toward
    # the space complexity of the algorithm.
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j = abs(nums[i])-1
            if nums[j] > 0:
                nums[j] *= - 1
        out = []
        for i in range(len(nums)):
            if nums[i] > 0:
                out.append(i + 1)
        return out
        
# @lc code=end

