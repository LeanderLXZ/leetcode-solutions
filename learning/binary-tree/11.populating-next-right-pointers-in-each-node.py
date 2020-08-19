#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (43.81%)
# Likes:    2157
# Dislikes: 145
# Total Accepted:    376K
# Total Submissions: 828.9K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
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
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000
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
    
    # def connect(self, root: 'Node') -> 'Node':
        
    #     stack = []
        
    #     def traversal(node, h):
    #         if node:
    #             if h == len(stack):
    #                 stack.append(node)
    #             else:
    #                 stack[h].next = node
    #                 stack[h] = node
    #             traversal(node.left, h+1)
    #             traversal(node.right, h+1)
    #             return node
        
    #     return traversal(root, 0)
    
    # Iterative
    # def connect(self, root: 'Node') -> 'Node':
    #     if root:
    #         cur_level = [root]
    #         while cur_level[0].left:
    #             pointer = cur_level[0].left
    #             next_level = []
    #             for i, cur in enumerate(cur_level):
    #                 if i != 0:
    #                     pointer.next = cur.left
    #                     pointer = cur.left
    #                 pointer.next = cur.right
    #                 pointer = cur.right
    #                 next_level.append(cur.left)
    #                 next_level.append(cur.right)
    #             cur_level = next_level
    #     return root
    
    # Iterative
    """
    while (!Q.empty())
    {
        size = Q.size()
        for i in range 0..size
        {
            node = Q.pop()
            Q.push(node.left)
            Q.push(node.right)
        }
    }
    """
    # def connect(self, root: 'Node') -> 'Node':
    #     if root:
    #         queue = [root]
    #         while queue[0]:
    #             size_queue = len(queue)
    #             for i in range(size_queue):
    #                 cur = queue.pop(0)
    #                 if i < size_queue - 1:
    #                     cur.next = queue[0]
    #                 queue.append(cur.left)
    #                 queue.append(cur.right)
    #         return root
        
    """
    leftmost = root
    while (leftmost.left != null)
    {
        head = leftmost
        while (head.next != null)
        {
            1) Establish Connection 1
            2) Establish Connection 2 using next pointers
            head = head.next
        }
        leftmost = leftmost.left
    }
    """
    def connect(self, root: 'Node') -> 'Node':
        if root:
            left_most = root
            while left_most.left:
                head = left_most
                while head:
                    head.left.next = head.right
                    if head.next:
                        head.right.next = head.next.left
                    head = head.next
                left_most = left_most.left
            return root
    
# @lc code=end

