#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (46.19%)
# Likes:    4010
# Dislikes: 409
# Total Accepted:    364.6K
# Total Submissions: 787.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# 
# 
# Example 4:
# 
# 
# Input: head = [1], k = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
# 
# 
# 
# Follow-up: Can you solve the problem in O(1) extra memory space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ans = ListNode(next=head)
        cache_list = [ans]
        while head:
            cache_list.append(head)
            head = head.next
            if len(cache_list) == k + 1:
                cache_list[0].next = cache_list[-1]
                cache_list.pop(0)
                for _ in range(k-1):
                    n = cache_list.pop()
                    n.next = cache_list[-1]
                cache_list[0].next = head
        return ans.next
        
# @lc code=end

