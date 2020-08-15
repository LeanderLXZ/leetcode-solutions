#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (46.32%)
# Likes:    4389
# Dislikes: 107
# Total Accepted:    681.2K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# Follow up: Solve it both recursively and iteratively.
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
    # def isSymmetric(self, root: TreeNode) -> bool:
        
    #     if root is None:
    #         return True
        
    #     def _symmetric(cur_l, cur_r):
    #         if not cur_l and not cur_r:
    #             return True
    #         if not cur_l or not cur_r:
    #             return False
    #         if cur_l.val == cur_r.val:
    #             return _symmetric(cur_l.left, cur_r.right) and \
    #                     _symmetric(cur_l.right, cur_r.left)
    #         else:
    #             return False
            
    #     return _symmetric(root.left, root.right)
    
    # Iterative
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            cur_l, cur_r = stack.pop()
            if not cur_l and not cur_r:
                continue
            if not cur_l or not cur_r:
                return False
            if cur_l.val == cur_r.val:
                stack.append((cur_l.right, cur_r.left))
                stack.append((cur_l.left, cur_r.right))
            else:
                return False
        return True
        
# @lc code=end

