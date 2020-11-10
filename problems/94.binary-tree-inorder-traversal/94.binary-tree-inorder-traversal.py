#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (62.28%)
# Likes:    3363
# Dislikes: 140
# Total Accepted:    765.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,3,2]
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
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     return [*self.inorderTraversal(root.left),
    #             root.val,
    #             *self.inorderTraversal(root.right)]
    
    # Iterative
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     out = []
    #     stack = [root]
    #     while stack:
    #         cur = stack[-1]
    #         if cur.left:
    #             stack.append(cur.left)
    #             cur.left = None
    #         else:
    #             out.append(stack.pop().val)
    #             if cur.right:
    #                 stack.append(cur.right)
    #                 cur.right = None
    #     return out
    
    # Optimal iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        out = []
        cur = root
        stack = []
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                out.append(cur.val)
                cur = cur.right
            else:
                break
        return out
        
# @lc code=end

