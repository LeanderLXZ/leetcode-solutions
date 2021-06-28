#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.88%)
# Likes:    11566
# Dislikes: 725
# Total Accepted:    1.4M
# Total Submissions: 4.4M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# 
# 
#

# @lc code=start
class Solution:
    
    # Dynamic Programming
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # def longestPalindrome(self, s: str) -> str:
    #     res = ''
    #     dp = [None] * len(s)
    #     for j in range(len(s)):
    #         for i in range(j+1):
    #             if i == j:
    #                 dp[i] = True
    #             elif j == i+1:
    #                 dp[i] = s[i] == s[j]
    #             else:
    #                 dp[i] = dp[i+1] and s[i] == s[j]
    #             if dp[i] and j - i + 1 > len(res):
    #                 res = s[i:j+1]
    #     return res
    
    
    # Expand Around Center
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    # def longestPalindrome(self, s: str) -> str:
    #     if s is '':
    #         return s
    #     max_len = 0
    #     start, end = 0, 0
    #     for i in range(len(s)):
    #         len1 = self.expandFromCenter(s, i, i)
    #         len2 = self.expandFromCenter(s, i, i+1)
    #         l = max(len1, len2)
    #         if l > end - start:
    #             start = i - (l - 1) // 2
    #             end = i + l // 2
    #     return s[start:end+1]

    # def expandFromCenter(self, s, idx1, idx2):
    #     while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
    #         idx1 -= 1
    #         idx2 += 1
    #     return idx2 - idx1 - 1
    
    
    # Longest Common Substring - DP
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return ""
        rev = s[::-1]
        dp = [0 for i in range(len(s))]
        max_len = 0
        max_end = 0
        for i in range(len(s)):
            # Updated the loop order
            for j in range(len(s)-1, -1, -1):
                if s[i] == rev[j]:
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0
                if dp[j] > max_len:
                    if i-dp[j]+1 == len(s)-1-j:
                        max_len = dp[j]
                        max_end = i
        return s[max_end - max_len + 1: max_end + 1]
    
    
    # Manacher’s Algorithm (O(n))
    # def longestPalindrome(self, s: str) -> str:
    #     N = len(s) 
    #     if N < 2: 
    #         return s
    #     N = 2*N+1    # Position count 
    #     L = [0] * N 
    #     L[0] = 0
    #     L[1] = 1
    #     C = 1     # centerPosition 
    #     R = 2     # centerRightPosition 
    #     i = 0    # currentRightPosition 
    #     iMirror = 0     # currentLeftPosition 
    #     maxLPSLength = 0
    #     maxLPSCenterPosition = 0
    #     start = -1
    #     end = -1
    #     diff = -1
   
    #     for i in range(2, N): 
    #         # get currentLeftPosition iMirror for currentRightPosition i 
    #         iMirror = 2*C-i 
    #         L[i] = 0
    #         diff = R - i 
    #         # If currentRightPosition i is within centerRightPosition R 
    #         if diff > 0: 
    #             L[i] = min(L[iMirror], diff) 
   
    #         # Attempt to expand palindrome centered at currentRightPosition i 
    #         # Here for odd positions, we compare characters and 
    #         # if match then increment LPS Length by ONE 
    #         # If even position, we just increment LPS by ONE without 
    #         # any character comparison 
    #         try:
    #             while ((i + L[i]) < N and (i - L[i]) > 0) \
    #                     and (((i + L[i] + 1) % 2 == 0) \
    #                     or (s[(i + L[i] + 1) // 2] == s[(i - L[i] - 1) // 2])): 
    #                 L[i]+=1
    #         except Exception as e:
    #             pass
                
    #         if L[i] > maxLPSLength:        # Track maxLPSLength 
    #             maxLPSLength = L[i] 
    #             maxLPSCenterPosition = i 
   
    #         # If palindrome centered at currentRightPosition i 
    #         # expand beyond centerRightPosition R, 
    #         # adjust centerPosition C based on expanded palindrome. 
    #         if i + L[i] > R: 
    #             C = i 
    #             R = i + L[i] 
   
    #     start = (maxLPSCenterPosition - maxLPSLength) // 2
    #     end = start + maxLPSLength - 1
    #     return s[start:end+1]
        
# @lc code=end

