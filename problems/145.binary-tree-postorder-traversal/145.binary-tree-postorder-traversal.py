#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (53.90%)
# Likes:    1920
# Dislikes: 96
# Total Accepted:    392.3K
# Total Submissions: 713K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     out = [*self.postorderTraversal(root.left),
    #            *self.postorderTraversal(root.right),
    #            root.val]
    #     return out

    # Iterative
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     out = []
    #     stack = [root]
    #     while stack:
    #         cur = stack[-1]
    #         if not cur.left and not cur.right:
    #             out.append(cur.val)
    #             stack.pop()
    #         elif cur.left:
    #             stack.append(cur.left)
    #             cur.left = None
    #         elif cur.right:
    #             stack.append(cur.right)
    #             cur.right = None
    #     return out
    
    # Optimal iterative
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        cur = root
        out = []
        stack = []
        while True:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if stack == []:
                out.append(cur.val)
                break
            if cur.right and stack[-1] == cur.right:
                stack.pop()
                stack.append(cur)
                cur = cur.right
            else:
                out.append(cur.val)
                cur = None
        return out
        
# @lc code=end

