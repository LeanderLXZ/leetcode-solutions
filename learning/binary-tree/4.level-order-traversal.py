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
    #             if len(out_list) <= h:
    #                 out_list.append([])
    #             out_list[h].append(node.val)
    #             traversal(node.left, h+1)
    #             traversal(node.right, h+1)
    #         else:
    #             return
        
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
            