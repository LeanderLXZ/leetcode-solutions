#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.01%)
# Likes:    3670
# Dislikes: 543
# Total Accepted:    912.7K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode(None)
        new_node = new_list
        while not (l1 is None or l2 is None):
            if l1.val < l2.val:
                new_node.next = l1
                l1 = l1.next
            else:
                new_node.next = l2
                l2 = l2.next
            new_node = new_node.next
        
        if l1 is None and l2 is not None:
            new_node.next = l2
        elif l1 is not None and l2 is None:
            new_node.next = l1
        
        return new_list.next
        
# @lc code=end

