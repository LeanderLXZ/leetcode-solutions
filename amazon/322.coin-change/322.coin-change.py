#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (38.13%)
# Likes:    7363
# Dislikes: 205
# Total Accepted:    676.3K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: coins = [1], amount = 1
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: coins = [1], amount = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    
    # Recursion with memory
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     self.memo = {0: 0}
    #     ret = self.helper(coins, amount)
    #     return ret if ret != float('inf') else -1
    
    # def helper(self, coins, remain):
    #     if remain in self.memo:
    #         return self.memo[remain]
    #     ret = float('inf')
    #     for c in coins:
    #         if remain >= c:
    #             ret = min(ret, self.helper(coins, remain - c) + 1)
    #     self.memo[remain] = ret
    #     return ret

    
    # Dynamic Programming
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [float('inf')] * (amount + 1)
    #     dp[0] = 0
    #     for i in range(amount + 1):
    #         for c in coins:
    #             if i >= c:
    #                 dp[i] = min(dp[i], dp[i-c] + 1)
    #     return dp[-1] if dp[-1] != float('inf') else -1
    
    
    # Dynamic Programming
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
            
            
        
# @lc code=end

