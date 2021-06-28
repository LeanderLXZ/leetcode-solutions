#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (42.48%)
# Likes:    5515
# Dislikes: 839
# Total Accepted:    587.7K
# Total Submissions: 1.4M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.
# 
# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new
# nodes should point to new nodes in the copied list such that the pointers in
# the original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.
# 
# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.
# 
# Return the head of the copied linked list.
# 
# The linked list is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
# 
# 
# Your code will only be given the head of the original linked list.
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# Example 4:
# 
# 
# Input: head = []
# Output: []
# Explanation: The given linked list is empty (null pointer), so return
# null.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 1000
# -10000 <= Node.val <= 10000
# Node.random is null or is pointing to some node in the linked list.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    # Recursion
    # Time Complexity: O(N)
    # where N is the number of nodes in the linked list.
    # Space Complexity: O(N)
    # If we look closely, we have the recursion stack and we also have the space
    # complexity to keep track of nodes already cloned i.e. using the visited 
    # dictionary. But asymptotically, the complexity is O(N).
    
    # visited = {}
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     if not head:
    #         return None
    #     if head in self.visited:
    #         return self.visited[head]
    #     new_node = Node(head.val, None, None)
    #     self.visited[head] = new_node
    #     new_node.next = self.copyRandomList(head.next)
    #     new_node.random = self.copyRandomList(head.random)
    #     return new_node

    
    # Iteration
    # Time Complexity : O(N)
    # because we make one pass over the original linked list.
    # Space Complexity : O(N)
    # as we have a dictionary containing mapping from old list nodes to new
    # list nodes. Since there are NN nodes, we have O(N)O(N) space complexity
    visited = {}
    def getClonedNode(self, node):
        if not node:
            return None
        if node not in self.visited:
            self.visited[node] = Node(node.val, None, None)
        return self.visited[node]

    def copyRandomList(self, head):
        if not head:
            return None

        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node != None:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]
    
    
    # Iterative with O(1) Space
    # Time Complexity : O(N)
    # Space Complexity : O(1)
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
    
# @lc code=end

