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
    
    def maxDepth(self, root: TreeNode) -> int:
        
        self.max_depth = 0

        def search(node, depth):
            if node:
                search(node.left, depth+1)
                search(node.right, depth+1)
            else:
                self.max_depth = max(self.max_depth, depth)
                
        search(root, self.max_depth)
        return self.max_depth
    