#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (49.53%)
# Likes:    2872
# Dislikes: 186
# Total Accepted:    525.9K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes. Only nodes itself may be
# changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
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
    
    # Recursive
    # Time Complexity: O(N) where NN is the size of the linked list.
    # Space Complexity: O(N) stack space utilized for recursion.
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = self.swapPairs(head.next.next)
        head.next.next = head
        head = head.next
        head.next.next = node
        return head
    
    # Iterative
    # Time Complexity : O(N) where N is the size of the linked list.
    # Space Complexity : O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        pre = None
        head = cur.next
        while cur and cur.next:
            first = cur
            second = cur.next
            first.next = second.next
            second.next = first
            if pre:
                pre.next = second
            cur, pre = first.next, first
        return head
        
# @lc code=end

