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
    
    
    # Recursive
    # Time Complexity: O(N)
    # since we process each node exactly twice. Once when we are counting the 
    # number of nodes in each recursive call, and then once when we are actually 
    # reversing the sub-list. A slightly optimized implementation here could be 
    # that we don't count the number of nodes at all and simply reverse k nodes.
    # If at any point we find that we didn't have enough nodes, we can 
    # re-reverse the last set of nodes so as to keep the original structure as 
    # required by the problem statement. That ways, we can get rid of the extra
    # counting.
    # Space Complexity: O(N/k) 
    # used up by the recursion stack. The number of recursion calls is 
    # determined by both kk and NN. In every recursive call, we process kk nodes 
    # and then make a recursive call to process the rest.
    def reverseLinkedList(self, head, k):
        
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains 
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next
            
            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr
            
            # Move on to the next node
            ptr = next_node
            
            # Decrement the count of nodes to be reversed by 1
            k -= 1
        
        # Return the head of the reversed list
        return new_head
                
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        count = 0
        ptr = head
        
        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        # If we have k nodes, then we reverse them
        if count == k: 
            
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            reversedHead = self.reverseLinkedList(head, k)
            
            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head
    
    
    # Iteration
    # Time Complexity: O(N)
    # since we process each node exactly twice. Once when we are counting the 
    # number of nodes in each recursive call, and then once when we are actually 
    # reversing the sub-list.
    # Space Complexity: O(1)
    def reverseLinkedList(self, head, k):
        
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains 
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next
            
            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr
            
            # Move on to the next node
            ptr = next_node
            
            # Decrement the count of nodes to be reversed by 1
            k -= 1
        
        # Return the head of the reversed list
        return new_head
                
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        ptr = head
        ktail = None
        
        # Head of the final, moified linked list
        new_head = None
        
        # Keep going until there are nodes in the list
        while ptr:
            count = 0
            
            # Start counting nodes from the head
            ptr = head
            
            # Find the head of the next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            # If we counted k nodes, reverse them        
            if count == k:
                
                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList(head, k)
                
                # new_head is the head of the final linked list
                if not new_head:
                    new_head = revHead
                
                # ktail is the tail of the previous block of 
                # reversed k nodes
                if ktail:
                    ktail.next = revHead
                    
                ktail = head 
                head = ptr
        
        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head
        
        return new_head if new_head else head
        
# @lc code=end

