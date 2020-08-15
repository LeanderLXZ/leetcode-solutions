#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (54.94%)
# Likes:    1637
# Dislikes: 61
# Total Accepted:    513.6K
# Total Submissions: 921.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,2,3]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
    
    # Recursive
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     out = [root.val, 
    #            *self.preorderTraversal(root.left), 
    #            *self.preorderTraversal(root.right)]
    #     return out
    
    # Iterative
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     out = []
    #     stack = [root]
    #     while stack:
    #         cur = stack.pop()
    #         out.append(cur.val)
    #         if cur.right:
    #             stack.append(cur.right)
    #         if cur.left:
    #             stack.append(cur.left)
    #     return out
    
    # Space Optimized
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur = root
        out = []
        stack = []
        while stack or cur:
            while cur:
                out.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            if stack:
                cur = stack.pop()
        return out
        
# @lc code=end

