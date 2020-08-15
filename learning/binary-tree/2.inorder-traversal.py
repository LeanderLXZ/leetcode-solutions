# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # Recursive
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     out = [*self.inorderTraversal(root.left),
    #            root.val,
    #            *self.inorderTraversal(root.right)]
    #     return out
    
    # Iterative
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     out = []
    #     stack = [root]
    #     while stack:
    #         cur = stack[-1]
    #         if cur.left:
    #             stack.append(cur.left)
    #             cur.left = None
    #         else:
    #             out.append(stack.pop().val)
    #             if cur.right:
    #                 stack.append(cur.right)
    #                 cur.right = None
    #     return out
    
    # Optimal iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        out = []
        cur = root
        stack = []
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                out.append(cur.val)
                cur = cur.right
            else:
                break
        return out