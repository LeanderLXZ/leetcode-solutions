#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
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

