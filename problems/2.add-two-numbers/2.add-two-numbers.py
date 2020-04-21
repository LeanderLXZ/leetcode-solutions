#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.10%)
# Likes:    7576
# Dislikes: 1952
# Total Accepted:    1.3M
# Total Submissions: 3.9M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def get_val(self, l):
        if l:
            l_val = l.val
            return l.next, l_val
        else:
            return l, 0
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pop = 0
        sum = ListNode(None)
        sum_copy = sum
        while l1 or l2:
            l1, l1_val = self.get_val(l1)
            l2, l2_val = self.get_val(l2)
            pop, sum_val = divmod(l1_val+l2_val+pop, 10)
            sum.next = ListNode(sum_val)
            sum = sum.next
        if pop > 0:
            sum.next = ListNode(pop)
        return sum_copy.next
        
# @lc code=end

