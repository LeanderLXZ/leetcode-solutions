#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (53.58%)
# Likes:    3247
# Dislikes: 78
# Total Accepted:    640.6K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    
    # Recursive
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     out_list = []
        
    #     def traversal(node, h):
    #         if node:
    #             if len(out_list) == h:
    #                 out_list.append([])
    #             out_list[h].append(node.val)
    #             traversal(node.left, h+1)
    #             traversal(node.right, h+1)
        
    #     traversal(root, 0)
    #     return out_list
        
    # Iterative
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        out_list = []
        cur_level = [root]
        while cur_level:
            out_list.append([n.val for n in cur_level])
            next_level = []
            for cur in cur_level:
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            cur_level = next_level
        return out_list
    
    # Iterative
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     out_list = []
    #     queue = [root]
    #     while queue:
    #         out_list.append([q.val for q in queue])
    #         for i in range(len(queue)):
    #             cur = queue.pop(0)
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)
                
    #     return out_list
        
# @lc code=end

