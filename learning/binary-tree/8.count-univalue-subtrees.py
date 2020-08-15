# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        self.count = 0
        
        def is_uni_value(node):
            if not node:
                return True, None
            b_l, v_l = is_uni_value(node.left)
            b_r, v_r = is_uni_value(node.right)
            if b_l and b_r and (v_l in [None, node.val]) and (v_r in [None, node.val]):
                self.count += 1
                return True, node.val
            return False, node.val
        
        is_uni_value(root)
        return self.count
    
    # def countUnivalSubtrees(self, root: TreeNode) -> int:
        
    #     self.count = 0
        
    #     def is_uni_value(node):
    #         if not node:
    #             return True
    #         left, right = is_uni_value(node.left), is_uni_value(node.right)
    #         if left and right and (not node.left or node.left.val == node.val) \
    #                 and (not node.right or node.right.val == node.val):
    #             self.count += 1
    #             return True
    #         return False
        
    #     is_uni_value(root)
    #     return self.count
    
    # def countUnivalSubtrees(self, root: TreeNode) -> int:
        
    #     self.count = 0
        
    #     def is_uni_value(node, parent):
    #         if not node:
    #             return True
    #         left = is_uni_value(node.left, node.val)
    #         right = is_uni_value(node.right, node.val)
    #         if left and right:
    #             self.count += 1
    #         return left and right and node.val == parent
        
    #     is_uni_value(root, None)
    #     return self.count