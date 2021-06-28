#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (61.37%)
# Likes:    5660
# Dislikes: 109
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        self.tail = None
        def helper(cur):
            if not cur.next:
                self.tail = cur
                return cur
            helper(cur.next).next = cur
            return cur
        helper(head).next = None
        return self.tail
    
    # Recursive
    # Time complexity : O(n)
    # Space complexity : O(n)
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
    # Iterative
    # Time complexity : O(n)
    # Space complexity : O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            second = cur.next
            cur.next = pre
            pre = cur
            cur = second
        return pre
        
# @lc code=end

