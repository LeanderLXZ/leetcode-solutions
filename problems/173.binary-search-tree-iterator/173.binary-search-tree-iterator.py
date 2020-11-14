#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (55.21%)
# Likes:    3004
# Dislikes: 286
# Total Accepted:    348.6K
# Total Submissions: 600.3K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
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
class BSTIterator:

    # Flatern inorder
    # O(N) is the time taken by the constructor for the iterator.
    # next() would take O(1)
    # hasNext() would take O(1)
    # Space complexity : O(N)
    # def __init__(self, root: TreeNode):
    #     self.inorder = []
    #     cur = root
    #     stack = []
    #     while True:
    #         if cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         elif stack:
    #             cur = stack.pop()
    #             self.inorder.append(cur.val)
    #             cur = cur.right
    #         else:
    #             break

    # def next(self) -> int:
    #     """
    #     @return the next smallest number
    #     """
    #     return self.inorder.pop(0)

    # def hasNext(self) -> bool:
    #     """
    #     @return whether we have a next smallest number
    #     """
    #     return bool(self.inorder)

    
    # Controlled Recursion
    def __init__(self, root: TreeNode):
        
        # Stack for the recursion simulation
        self.stack = []
        
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root):
        
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        # Need to maintain the invariant. If the node has a right child, call the 
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

