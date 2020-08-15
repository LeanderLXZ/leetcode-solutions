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