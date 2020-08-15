#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (40.60%)
# Likes:    2112
# Dislikes: 514
# Total Accepted:    492.4K
# Total Submissions: 1.2M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
#
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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

    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
    #     if not root:
    #         return False
        
    #     def traversal(node, acc):
    #         acc += node.val
    #         if not node.left and not node.right:
    #             return acc == sum
    #         if node.left:
    #             left = traversal(node.left, acc)
    #         else:
    #             left = False
    #         if node.right:
    #             right = traversal(node.right, acc)
    #         else:
    #             right = False
    #         return left or right
        
    #     return traversal(root, 0)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
# @lc code=end

