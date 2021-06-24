#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (56.95%)
# Likes:    7200
# Dislikes: 799
# Total Accepted:    1.5M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a sorted list. The list should
# be made by splicing together the nodes of the first two lists.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# 
# Input: l1 = [], l2 = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: l1 = [], l2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Iteration
    # Time complexity : O(n+m)
    # Because exactly one of l1 and l2 is incremented on each loop iteration,
    # the while loop runs for a number of iterations equal to the sum of the
    # lengths of the two lists. All other work is constant, so the overall
    # complexity is linear.
    # Space complexity : O(1)
    # The iterative approach only allocates a few pointers, so it has a constant
    # overall memory footprint.
    def append_tail(self,tail, l):
        tail.next = l
        return tail.next, l.next
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        ans_tail = ans
        while l1 or l2:
            if l1 and l2:
                if l1.val >= l2.val:
                    ans_tail, l2 = self.append_tail(ans_tail, l2)
                else:
                    ans_tail, l1 = self.append_tail(ans_tail, l1)
            elif l1 and not l2:
                ans_tail, l1 = self.append_tail(ans_tail, l1)
            else:
                ans_tail, l2 = self.append_tail(ans_tail, l2)
        return ans.next
    
    # Recursion
    # Time complexity : O(n+m)
    # Because each recursive call increments the pointer to l1 or l2 by one 
    # (approaching the dangling null at the end of each list), there will be
    # exactly one call to mergeTwoLists per element in each list. Therefore,
    # the time complexity is linear in the combined size of the lists.
    # Space complexity : O(n+m)
    # The first call to mergeTwoLists does not return until the ends of both l1 
    # and l2 have been reached, so n+m stack frames consume O(n+m) space.
    # def mergeTwoLists(self, l1, l2):
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1
    #     elif l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

# @lc code=end

