#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.50%)
# Likes:    4805
# Dislikes: 596
# Total Accepted:    808.8K
# Total Submissions: 2.9M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
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

    # Recursive O(N) / O(N)
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            if not helper(node.left, low, node.val):
                return False
            if not helper(node.right, node.val, high):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))
    
    # Iterative O(N) / O(N)
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()
            if node.val <= low or node.val >= high:
                return False
            if node.left:
                stack.append((node.left, low, node.val))
            if node.right:
                stack.append((node.right, node.val, high))
        return True

# @lc code=end

