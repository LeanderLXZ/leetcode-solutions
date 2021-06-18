#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
# https://leetcode.com/problems/most-common-word/description/
#
# algorithms
# Easy (45.43%)
# Likes:    1002
# Dislikes: 2157
# Total Accepted:    236.8K
# Total Submissions: 521.5K
# Testcase Example:  '"Bob hit a ball, the hit BALL flew far after it was hit."\n["hit"]'
#
# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned. It is guaranteed there is
# at least one word that is not banned, and that the answer is unique.
# 
# The words in paragraph are case-insensitive and the answer should be returned
# in lowercase.
# 
# 
# Example 1:
# 
# 
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent
# non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is
# banned.
# 
# 
# Example 2:
# 
# 
# Input: paragraph = "a.", banned = []
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols:
# "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    
    # String Processing in Pipeline
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = ''.join([' ' if c in '!?\',;.' else c.lower() for c in paragraph])
        count = collections.defaultdict(int)
        banned_words = set(banned)
        for word in paragraph.split():
            if word not in banned_words:
                count[word] += 1
        return max(count, key=count.get)
    
    
    # String Processing in Pipeline
    # Let N be the number of characters in the input string and 
    # M be the number of characters in the banned list.
    # Time Complexity: O(N+M)
    # Space Complexity: O(N+M)
    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     #1). replace the punctuations with spaces,
    #     #      and put all letters in lower case
    #     normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

    #     #2). split the string into words
    #     words = normalized_str.split()

    #     word_count = defaultdict(int)
    #     banned_words = set(banned)

    #     #3). count the appearance of each word, excluding the banned words
    #     for word in words:
    #         if word not in banned_words:
    #             word_count[word] += 1

    #     #4). return the word with the highest frequency
    #     return max(word_count.items(), key=operator.itemgetter(1))[0]
    

    # Character Processing in One-Pass
    # Let N be the number of characters in the input string and 
    # M be the number of characters in the banned list.
    # Time Complexity: O(N+M)
    # Space Complexity: O(N+M)
    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

    #     banned_words = set(banned)
    #     ans = ""
    #     max_count = 0
    #     word_count = defaultdict(int)
    #     word_buffer = []

    #     for p, char in enumerate(paragraph):
    #         #1). consume the characters in a word
    #         if char.isalnum():
    #             word_buffer.append(char.lower())
    #             if p != len(paragraph)-1:
    #                 continue

    #         #2). at the end of one word or at the end of paragraph
    #         if len(word_buffer) > 0:
    #             word = "".join(word_buffer)
    #             if word not in banned_words:
    #                 word_count[word] +=1
    #                 if word_count[word] > max_count:
    #                     max_count = word_count[word]
    #                     ans = word
    #             # reset the buffer for the next word
    #             word_buffer = []

    #     return ans
        
# @lc code=end

