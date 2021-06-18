#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (28.69%)
# Likes:    11151
# Dislikes: 1111
# Total Accepted:    1.3M
# Total Submissions: 4.7M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:

    # Two pointers
    # Time Complexity: O(n^2)
    # Space Complexity: from O(logn) to O(n)
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums_sorted = sorted(nums)
    #     for i, n in enumerate(nums_sorted):
    #         if n > 0:
    #             break
    #         if i == 0 or n != nums_sorted[i-1]:
    #             remain = nums_sorted[i+1:]
    #             left, right = 0, len(remain) - 1
    #             while left < right:
    #                 sum_ = remain[left] + remain[right] + n
    #                 if sum_ == 0:
    #                     res.append([n, remain[left], remain[right]])
    #                     left += 1
    #                     right -= 1
    #                     while left < right and remain[left] == remain[left - 1]:
    #                         left += 1
    #                 elif sum_ < 0:
    #                     left += 1
    #                 else:
    #                     right -= 1
    #     return res
    
    # Hashset
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums_sorted = sorted(nums)
    #     for i, n in enumerate(nums_sorted):
    #         if n > 0:
    #             break
    #         if i == 0 or n != nums_sorted[i-1]:
    #             remain, j = nums_sorted[i+1:], 0
    #             seen = set()
    #             while j < len(remain):
    #                 diff = - n - remain[j]
    #                 if diff in seen:
    #                     res.append([n, remain[j], diff])
    #                     while j < len(remain) - 1 and remain[j] == remain[j+1]:
    #                         j += 1
    #                 seen.add(remain[j])
    #                 j += 1
    #     return res

    # Hashset
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums_sorted = sorted(nums)
    #     for i, n in enumerate(nums_sorted):
    #         if n > 0:
    #             break
    #         if i == 0 or n != nums_sorted[i-1]:
    #             seen = set()
    #             j = i + 1
    #             while j < len(nums_sorted):
    #                 complement = -nums_sorted[i] - nums_sorted[j]
    #                 if complement in seen:
    #                     res.append([nums_sorted[i], nums_sorted[j], complement])
    #                     while j + 1 < len(nums_sorted) and nums_sorted[j] == nums_sorted[j + 1]:
    #                         j += 1
    #                 seen.add(nums_sorted[j])
    #                 j += 1
    #     return res
    
    # No-sort
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res, dups = set(), set()
        
    #     for i, n in enumerate(nums):
    #         if n not in dups:
    #             dups.add(n)
    #             seen = set()
    #             for m in nums[i+1:]:
    #                 diff = - n - m
    #                 if diff in seen:
    #                     res.add(tuple(sorted([n, m, diff])))
    #                 seen.add(m)
    #     return res
    
    # Optimized No-sort
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res

        
# @lc code=end

