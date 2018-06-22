#
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s):
        str_map = dict()
        i = j = max_len = 0
        max_range = []
        for j in range(len(s)):
            if s[j] in str_map:
                i = str_map[s[j]] + 1
                str_map[s[j]] = j
            else:
                str_map[s[j]] = j
                # max_len = max(max_len, j-i+1)
                # try to output the longest substring
                if max_len < j - i + 1:
                    max_len = j - i + 1
                    max_range = [(i, j)]
                elif max_len == j - i + 1:
                    max_range.append((i, j))
        print("max length: ", max_len)
        for i in max_range:
            print("max substring: ", s[i[0]:i[1] + 1])
            print("substring index are: ", max_range, end="\n\n")
        return max_len


sol = Solution()
a = "abcabcbb"
sol.lengthOfLongestSubstring(a)

a = "bbbbb"
sol.lengthOfLongestSubstring(a)

a = "pwwkew"
sol.lengthOfLongestSubstring(a)
