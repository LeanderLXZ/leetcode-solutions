#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (44.60%)
# Likes:    1948
# Dislikes: 37
# Total Accepted:    245.3K
# Total Submissions: 519.4K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        dict_inorder = {v:i for i, v in enumerate(inorder)}
        
        def build(idx_left, idx_right):
            
            if idx_left > idx_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            idx_root = dict_inorder[val]
            
            root.right = build(idx_root+1, idx_right)
            root.left = build(idx_left, idx_root-1)
            
            return root
        
        return build(0, len(inorder)-1)
    
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
    #     def build(bound=None):
            
    #         if not inorder or inorder[-1] == bound:
    #             return None
            
    #         root = TreeNode(postorder.pop())
    #         root.right = build(root.val)
    #         inorder.pop()
    #         root.left = build(bound)
    #         return root

    #     return build()
        
# @lc code=end

