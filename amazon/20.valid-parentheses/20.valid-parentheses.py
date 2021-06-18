#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.32%)
# Likes:    4500
# Dislikes: 206
# Total Accepted:    921.8K
# Total Submissions: 2.4M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
        
    # def isValid(self, s: str) -> bool:
    #     left = ['(', '{', '[']
    #     right = [')', '}', ']']
    #     par_opened = []
    #     for s_i in s:
    #         if s_i in left:
    #             par_opened.append(s_i)
    #         elif par_opened and (par_opened[-1], s_i) in list(zip(left, right)):
    #             par_opened.pop()
    #         else:
    #             return False
    #     if par_opened:
    #         return False
    #     return True
    
    
    # Time complexity : O(n) 
    # because we simply traverse the given string one character at a time and 
    # push and pop operations on a stack take O(1) time.
    # Space complexity : O(n) as we push all opening brackets onto the stack 
    # and in the worst case, we will end up pushing all the brackets onto 
    # the stack. e.g. ((((((((((.
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
        
# @lc code=end

