#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#
# https://leetcode.com/problems/inorder-successor-in-bst/description/
#
# algorithms
# Medium
#
# Given a binary search tree and a node in it, find the in-order successor of
# that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than
# p.val.
#
#
#
#
#
# Example 1:
#
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return
# value is of TreeNode type.
#
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer
# is null.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        self.suc = None
        def helper(node):
            if not node:
                return
            if node.val > p.val:
                self.suc = node
                helper(node.left)
            if node.val <= p.val:
                helper(node.right)
        helper(root)
        return self.suc
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        suc = None
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val > p.val:
                suc = node
                stack.append(node.left)
            if node.val <= p.val:
                stack.append(node.right)
        return suc
    
    # O(H) / O(1)
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        # the successor is somewhere upper in the tree
        stack, inorder = [], float('-inf')
        
        # inorder traversal : left -> node -> right
        while stack or root:
            # 1. go left till you can
            while root:
                stack.append(root)
                root = root.left
                
            # 2. all logic around the node
            root = stack.pop()
            if inorder == p.val:    # if the previous node was equal to p
                return root         # then the current node is its successor
            inorder = root.val
            
            # 3. go one step right
            root = root.right

        # there is no successor
        return None
    
    # Another iterative inorder tranversal version
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        stack = []
        cur = root
        pre_node = None
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                if pre_node == p:
                    return cur
                pre_node = cur
                cur = cur.right
            else:
                break
        return None


# @lc code=end

