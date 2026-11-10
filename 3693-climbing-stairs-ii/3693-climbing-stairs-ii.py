
class Solution:
    def climbStairs(self, n, costs):
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = float('inf')

            for j in range(1, 4):
                if i >= j:
                    dp[i] = min(
                        dp[i],
                        dp[i - j] + costs[i - 1] + j * j
                    )

        return dp[n]
