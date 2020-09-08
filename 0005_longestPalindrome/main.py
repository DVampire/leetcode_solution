class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n=len(s)
        if n<=1:
            return s

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        res = s[0]
        longest = 1
        for j in range(1,len(s)):
            for i in range(j):
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    cur_len = j-i+1
                    if cur_len>longest:
                        longest=cur_len
                        res = s[i:j+1]
        return res

class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]