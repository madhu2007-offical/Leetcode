class Solution {
    static final int MOD = 1_000_000_007;

    public int numberOfSets(int n, int k) {
        long[][] dp = new long[k + 1][n];

        // dp[j][i] = number of ways to make j segments
        // using points 0...i
        for (int i = 0; i < n; i++) {
            dp[0][i] = 1;
        }

        for (int j = 1; j <= k; j++) {
            long prefix = 0;

            for (int i = 0; i < n; i++) {

                // Ways where we don't use i as the endpoint
                if (i > 0) {
                    dp[j][i] = dp[j][i - 1];
                }

                // Add ways where a segment ends at i.
                // Segment must have length >= 1,
                // so its starting point is at most i-1.
                if (i >= 1) {
                    prefix = (prefix + dp[j - 1][i - 1]) % MOD;
                    dp[j][i] = (dp[j][i] + prefix) % MOD;
                }
            }
        }

        return (int) dp[k][n - 1];
    }
}