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
        