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
    