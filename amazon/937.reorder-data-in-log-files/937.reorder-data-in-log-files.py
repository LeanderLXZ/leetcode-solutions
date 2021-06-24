#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#
# https://leetcode.com/problems/reorder-data-in-log-files/description/
#
# algorithms
# Easy (55.07%)
# Likes:    1147
# Dislikes: 3012
# Total Accepted:    217.6K
# Total Submissions: 395.1K
# Testcase Example:  '["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]'
#
# You are given an array of logs. Each log is a space-delimited string of
# words, where the first word is the identifier.
# 
# There are two types of logs:
# 
# 
# Letter-logs: All words (except the identifier) consist of lowercase English
# letters.
# Digit-logs: All words (except the identifier) consist of digits.
# 
# 
# Reorder these logs so that:
# 
# 
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their
# contents are the same, then sort them lexicographically by their
# identifiers.
# The digit-logs maintain their relative ordering.
# 
# 
# Return the final order of the logs.
# 
# 
# Example 1:
# 
# 
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit
# dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5
# 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can",
# "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
# 
# 
# Example 2:
# 
# 
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act
# zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4
# 7"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# All the tokens of logs[i] are separated by a single space.
# logs[i] is guaranteed to have an identifier and at least one word after the
# identifier.
# 
# 
#

# @lc code=start
class Solution:

    # Let N be the number of logs in the list and M be the maximum length of a single log.

    # Time Complexity: O(M⋅N⋅logN)
    # The sorted() in Python is implemented with the Timsort algorithm whose 
    # time complexity is O(N⋅logN).
    # Since the keys of the elements are basically the logs itself, the 
    # comparison between two keys can take up to O(M) time.
    # Therefore, the overall time complexity of the algorithm is O(M⋅N⋅logN).

    # Space Complexity: O(M⋅N)
    # First, we need O(M⋅N) space to keep the keys for the log.
    # In addition, the worst space complexity of the Timsort algorithm is O(N),
    # assuming that the space for each element is O(1). 
    # Hence we would need O(M⋅N) space to hold the intermediate values for sorting.
    # In total, the overall space complexity of the algorithm isO(M⋅N+M⋅N)=O(M⋅N).
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
        
# @lc code=end

