class Solution {
public:
    int n;
    vector<int> suffix;
    vector<vector<int>> dp;

    int solve(int i, int M) {
        if (i >= n)
            return 0;

        if (dp[i][M] != -1)
            return dp[i][M];

        int best = 0;

        // Can take X piles, where 1 <= X <= 2*M
        for (int X = 1; X <= 2 * M && i + X <= n; X++) {
            // Stones taken now
            int taken = suffix[i] - suffix[i + X];

            // Opponent gets the best possible result from remaining piles
            int opponent = solve(i + X, max(M, X));

            // Total stones we can eventually get
            int total = taken + (suffix[i + X] - opponent);

            best = max(best, total);
        }

        return dp[i][M] = best;
    }

    int stoneGameII(vector<int>& piles) {
        n = piles.size();

        // suffix[i] = total stones from i to n-1
        suffix.assign(n + 1, 0);

        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + piles[i];
        }

        dp.assign(n, vector<int>(n + 1, -1));

        return solve(0, 1);
    }
};