#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (65.22%)
# Likes:    2702
# Dislikes: 78
# Total Accepted:    858.9K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its depth = 3.
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
    
    # def maxDepth(self, root: TreeNode) -> int:
    #     def search(node, depth):
    #         if node is None:
    #             return depth
    #         return max(search(node.left, depth), search(node.right, depth)) + 1
    #     return search(root, 0)

    # def maxDepth(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     return max(self.maxDepth(root.left),  self.maxDepth(root.right)) + 1

    # def maxDepth(self, root: TreeNode) -> int:
    #     return max(map(self.maxDepth, [root.left, root.right])) + 1 if root else 0
    
    # def maxDepth(self, root: TreeNode) -> int:
    #     self.max_depth = 0
    #     def search(node, depth):
    #         if node:
    #             search(node.left, depth+1)
    #             search(node.right, depth+1)
    #         else:
    #             self.max_depth = max(self.max_depth, depth)
    #     search(root, self.max_depth)
    #     return self.max_depth
    
    # Iterative
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_depth, cur = stack.pop()
            if cur:
                depth = max(cur_depth, depth)
                stack.append((cur_depth + 1, cur.left))
                stack.append((cur_depth + 1, cur.right))
        return depth
    
        
# @lc code=end

