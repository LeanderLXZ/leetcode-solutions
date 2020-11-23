#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (38.14%)
# Likes:    2961
# Dislikes: 159
# Total Accepted:    306K
# Total Submissions: 769K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre, end, end_pre, cur, i = None, None, None, head, 1
        out = None if m == 1 else head
        while cur:
            nex = cur.next
            if m <= i <= n:
                cur.next = pre
                if i == m:
                    end = cur
                    end_pre = pre
                if i == n:
                    if nex and not out:
                        out = cur
                    if end_pre:
                        end_pre.next = cur
                    end.next = nex
            pre, cur = cur, nex
            i += 1
        return pre if not out else out
    
    # Time Complexity: O(N) since we process all the nodes at-most twice.
    # Once during the normal recursion process and once during the backtracking
    # process. During the backtracking process we only just swap half of the
    # list if you think about it, but the overall complexity is O(N).
    # Space Complexity: O(N) in the worst case when we have to reverse the
    # entire list. This is the space occupied by the recursion stack.
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head
    
    # Time Complexity: O(N) considering the list consists of NN nodes. We
    # process each of the nodes at most once (we don't process the nodes
    # after the n^{th} node from the beginning.
    # Space Complexity: O(1) since we simply adjust some pointers in the
    # original linked list and only use O(1)O(1) additional memory for
    # achieving the final result.
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
        
# @lc code=end

