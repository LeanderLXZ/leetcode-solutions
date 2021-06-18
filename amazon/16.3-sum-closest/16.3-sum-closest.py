#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.43%)
# Likes:    3465
# Dislikes: 181
# Total Accepted:    599K
# Total Submissions: 1.3M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 =
# 2).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    
    # Time Complexity: O(n^2)
    # Space Complexity: from O(logn) to O(n)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        for i, n in enumerate(nums):
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] + n
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return target
        return target - diff
    
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     res, least_diff = None, float('inf')
    #     for i, n in enumerate(nums):
    #         left, right = i+1, len(nums)-1
    #         while left < right:
    #             diff = target - nums[left] - nums[right] - n
    #             if abs(diff) < least_diff:
    #                 res = nums[left] + nums[right] + n
    #                 least_diff = abs(diff)
    #             if diff > 0:
    #                 left += 1
    #             elif diff < 0:
    #                 right -= 1
    #             else:
    #                 return res
    #     return res
    
    # Binary search
    # Time Complexity: O(n^2logn)
    # Space Complexity: from O(logn) to O(n)
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     diff = float('inf')
    #     nums.sort()
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             complement = target - nums[i] - nums[j]
    #             hi = bisect_right(nums, complement, j + 1)
    #             lo = hi - 1
    #             if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
    #                 diff = complement - nums[hi]
    #             if lo > j and abs(complement - nums[lo]) < abs(diff):
    #                 diff = complement - nums[lo]
    #         if diff == 0:
    #             break
    #     return target - diff
        
# @lc code=end

