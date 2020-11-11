#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (38.22%)
# Likes:    1678
# Dislikes: 182
# Total Accepted:    261.8K
# Total Submissions: 667.2K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
#
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Follow up:
#
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
#
#
#
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100
#
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:

    # Iterative BFS
    def connect(self, root: 'Node') -> 'Node':
        if root:
            queue = [root]
            while queue:
                size_queue = len(queue)
                for i in range(size_queue):
                    cur = queue.pop(0)
                    if i < size_queue - 1:
                        cur.next = queue[0]
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            return root
    
    # def add_node(self, node):
    #     self.pointers.append(node)
    #     if not self.left_most:
    #         self.left_most = node
    #     if len(self.pointers) > 1:
    #         left = self.pointers.pop(0)
    #         left.next = self.pointers[0]
        
    # def connect(self, root: 'Node') -> 'Node':
    #     if root:
    #         self.left_most = root
    #         while self.left_most:
    #             head, self.pointers = self.left_most, []
    #             self.left_most = None
    #             while head:
    #                 if head.left:
    #                     self.add_node(head.left)
    #                 if head.right:
    #                     self.add_node(head.right)
    #                 head = head.next
    #         return root
            
    
    """
    leftmost = root
    while (leftmost != null)
    {
        curr = leftmost
        prev = NULL
        while (curr != null)
        {
            → process left child
            → process right child
            → set leftmost for the next level
            curr = curr.next
        }
    }
    """
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            
            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        
        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                
                # Move onto the next node.
                curr = curr.next
                
        return root
        
# @lc code=end

