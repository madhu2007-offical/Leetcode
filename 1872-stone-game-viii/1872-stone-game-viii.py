class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        dp = [0] * n
        dp[n - 1] = prefix[n - 1]

        for i in range(n - 2, 0, -1):
            dp[i] = max(dp[i + 1], prefix[i] - dp[i + 1])

        return dp[1]
