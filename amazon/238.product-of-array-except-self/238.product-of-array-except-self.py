#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (61.63%)
# Likes:    7761
# Dislikes: 572
# Total Accepted:    800.4K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
# 
#

# @lc code=start
class Solution:
    
    # Left and Right product lists
    # Time complexity : O(N) 
    # where N represents the number of elements in the input array. We use one 
    # iteration to construct the array L, one to construct the array R and one 
    # last to construct the answeranswer array using L and R.
    # Space complexity : O(N)
    # used up by the two intermediate arrays that we constructed to keep 
    # track of product of elements to the left and right.
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     p_l, p_r = [1], [1]
    #     for i in range(len(nums)-1):
    #         p_l.append(p_l[i] * nums[i])
    #         p_r.append(p_r[i] * nums[-i-1])
    #     return [l * r for l, r in zip(p_l, p_r[::-1])]


    # Time complexity : O(N) 
    # where N represents the number of elements in the input array. 
    # We use one iteration to construct the array L, 
    # one to update the array answeranswer.
    # Space complexity : O(1) 
    # since don't use any additional array for our computations. 
    # The problem statement mentions that using the answeranswer array 
    # doesn't add to the space complexity.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for i in range(n - 1):
            ans[i+1] = ans[i] * nums[i]
        r = 1
        for i in range(n - 1):
            r *= nums[-i-1]
            ans[-i-2] *= r
        return ans
    
    
    # Left and Right product lists
    # Time complexity : O(N) 
    # where N represents the number of elements in the input array. We use one 
    # iteration to construct the array L, one to construct the array R and one 
    # last to construct the answeranswer array using L and R.
    # Space complexity : O(N)
    # used up by the two intermediate arrays that we constructed to keep 
    # track of product of elements to the left and right.
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    #     # The length of the input array 
    #     length = len(nums)
        
    #     # The left and right arrays as described in the algorithm
    #     L, R, answer = [0]*length, [0]*length, [0]*length
        
    #     # L[i] contains the product of all the elements to the left
    #     # Note: for the element at index '0', there are no elements to the left,
    #     # so the L[0] would be 1
    #     L[0] = 1
    #     for i in range(1, length):
            
    #         # L[i - 1] already contains the product of elements to the left of 'i - 1'
    #         # Simply multiplying it with nums[i - 1] would give the product of all 
    #         # elements to the left of index 'i'
    #         L[i] = nums[i - 1] * L[i - 1]
        
    #     # R[i] contains the product of all the elements to the right
    #     # Note: for the element at index 'length - 1', there are no elements to the right,
    #     # so the R[length - 1] would be 1
    #     R[length - 1] = 1
    #     for i in reversed(range(length - 1)):
            
    #         # R[i + 1] already contains the product of elements to the right of 'i + 1'
    #         # Simply multiplying it with nums[i + 1] would give the product of all 
    #         # elements to the right of index 'i'
    #         R[i] = nums[i + 1] * R[i + 1]
        
    #     # Constructing the answer array
    #     for i in range(length):
    #         # For the first element, R[i] would be product except self
    #         # For the last element of the array, product except self would be L[i]
    #         # Else, multiple product of all elements to the left and to the right
    #         answer[i] = L[i] * R[i]
        
    #     return answer
    
    
    # Time complexity : O(N) 
    # where N represents the number of elements in the input array. 
    # We use one iteration to construct the array L, 
    # one to update the array answeranswer.
    # Space complexity : O(1) 
    # since don't use any additional array for our computations. 
    # The problem statement mentions that using the answeranswer array 
    # doesn't add to the space complexity.
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    #     # The length of the input array 
    #     length = len(nums)
        
    #     # The answer array to be returned
    #     answer = [0]*length
        
    #     # answer[i] contains the product of all the elements to the left
    #     # Note: for the element at index '0', there are no elements to the left,
    #     # so the answer[0] would be 1
    #     answer[0] = 1
    #     for i in range(1, length):
            
    #         # answer[i - 1] already contains the product of elements to the left of 'i - 1'
    #         # Simply multiplying it with nums[i - 1] would give the product of all 
    #         # elements to the left of index 'i'
    #         answer[i] = nums[i - 1] * answer[i - 1]
        
    #     # R contains the product of all the elements to the right
    #     # Note: for the element at index 'length - 1', there are no elements to the right,
    #     # so the R would be 1
    #     R = 1;
    #     for i in reversed(range(length)):
            
    #         # For the index 'i', R would contain the 
    #         # product of all elements to the right. We update R accordingly
    #         answer[i] = answer[i] * R
    #         R *= nums[i]
        
    #     return answer
    
# @lc code=end

