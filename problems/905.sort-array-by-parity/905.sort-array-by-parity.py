#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (73.88%)
# Likes:    1392
# Dislikes: 80
# Total Accepted:    272.1K
# Total Submissions: 363.3K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#
#
#
# Example 1:
#
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
#
#
#

# @lc code=start
class Solution:
    
    # Sort
    # Time Complexity: O(NlogN), where N is the length of A.
    # Space Complexity: O(N) for the sort, depending on the built-in implementation of sort.
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A
    
    # Two pass
    # Time Complexity: O(N), where NN is the length of A.
    # Space Complexity: O(N), the space used by the answer.
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
    
    # Swap
    # Space Complexity : O(1). Only constant space is used.
    # Time Complexity: O(n)
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i_odd = 0
        for i in range(len(A)):
            if not A[i] % 2:
                A[i], A[i_odd] = A[i_odd], A[i]
                i_odd += 1
        return A
        
# @lc code=end

