#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:

    def reverse(self, x: int) -> int:
        int_max = 2**31 - 1
        x_abs = abs(x)
        num_list = []
        x_reversed = 0
        while x_abs != 0:
            x_abs, c = divmod(x_abs, 10)
            x_reversed = x_reversed * 10 + c
            if x_reversed > 2**31 - 1:
                return 0
        if x < 0:
            return x_reversed * -1
        else:
            return x_reversed
        
# @lc code=end

