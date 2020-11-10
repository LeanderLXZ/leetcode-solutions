#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (47.51%)
# Likes:    3645
# Dislikes: 98
# Total Accepted:    377.9K
# Total Submissions: 772.2K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     dict_inorder = {v:i for i, v in enumerate(inorder)}
    #     def build(idx_left, idx_right):
    #         if idx_left > idx_right:
    #             return None
    #         val = preorder.pop(0)
    #         root = TreeNode(val)
    #         idx_root = dict_inorder[val] 
    #         root.left = build(idx_left, idx_root-1)
    #         root.right= build(idx_root+1, idx_right)
    #         return root
    #     return build(0, len(inorder)-1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def build(bound=None):
            if not inorder or inorder[0] == bound:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = build(root.val)
            inorder.pop(0)
            root.right = build(bound)
            return root

        return build()

# @lc code=end

