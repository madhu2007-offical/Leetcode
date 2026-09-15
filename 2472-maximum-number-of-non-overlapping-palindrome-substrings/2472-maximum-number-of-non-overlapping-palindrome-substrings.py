class Solution(object):

    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum number of palindromes
        # that can be selected from s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Skip current character
            dp[i] = dp[i - 1]

            # Try palindrome ending at i - 1
            for j in range(i - k + 1):
                if i - j >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]