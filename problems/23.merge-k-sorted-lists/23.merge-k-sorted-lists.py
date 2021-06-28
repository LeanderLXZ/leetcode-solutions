#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (43.66%)
# Likes:    7681
# Dislikes: 364
# Total Accepted:    916.1K
# Total Submissions: 2.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
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
   
    # Merge with Divide And Conquer
    # Time complexity : O(Nlogk) 
    # where k is the number of linked lists.
    # We can merge two sorted linked list in O(n) time where n is the total 
    # number of nodes in two lists. Sum up the merge process and we can get: 
    # O(∑_(i=1)(log_2k)N)=O(Nlogk)
    # Space complexity : O(1)
    # We can merge two sorted linked lists in O(1) space.
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     amount = len(lists)
    #     interval = 1
    #     while interval < amount:
    #         for i in range(0, amount - interval, interval * 2):
    #             lists[i] = self.merge2Lists(lists[i], lists[i + interval])
    #         interval *= 2
    #     return lists[0] if amount > 0 else None

    # def merge2Lists(self, l1, l2):
    #     head = point = ListNode(0)
    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             point.next = l1
    #             l1 = l1.next
    #         else:
    #             point.next = l2
    #             l2 = l1
    #             l1 = point.next.next
    #         point = point.next
    #     if not l1:
    #         point.next=l2
    #     else:
    #         point.next=l1
    
    # Heap queue
    # Time complexity : O(Nlogk) 
    # where k is the number of linked lists.
    # The comparison cost will be reduced to O(logk) for every pop and insertion
    # to priority queue. But finding the node with the smallest value just costs
    # O(1) time. There are N nodes in the final linked list.
    # Space complexity : O(n)
    # Creating a new linked list costs O(n) space.
    # O(k) The code above present applies in-place method which cost O(1)
    # space. And the priority queue (often implemented with heaps) costs O(k)
    # space (it's far less than N in most situations).
    def mergeKLists(self, lists):
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
    
    
    # Merge sort
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    
    #     def merge(lst1, lst2):
    #         dummy = pt = ListNode(-1)
    #         while lst1 and lst2:
    #             if lst1.val < lst2.val:
    #                 pt.next = lst1
    #                 lst1 = lst1.next
    #             else:
    #                 pt.next = lst2
    #                 lst2 = lst2.next
    #             pt = pt.next
                
    #         pt.next = lst1 if not lst2 else lst2
    #         return dummy.next
            
    #     if not lists:
    #         return None

    #     if len(lists) == 1:
    #         return lists[0]
    #     mid = len(lists)/2
    #     left = self.mergeKLists(lists[:mid])
    #     right = self.mergeKLists(lists[mid:])

    #     return merge(left, right)
        
# @lc code=end

