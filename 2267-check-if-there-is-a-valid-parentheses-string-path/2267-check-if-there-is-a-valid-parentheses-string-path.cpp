class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        // Path length must be even
        if ((m + n - 1) % 2 != 0)
            return false;

        // dp[j] stores possible balances at cell (i, j)
        vector<vector<unordered_set<int>>> dp(
            m, vector<unordered_set<int>>(n)
        );

        // Starting cell
        if (grid[0][0] == '(')
            dp[0][0].insert(1);
        else
            return false;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (i == 0 && j == 0)
                    continue;

                unordered_set<int> possible;

                // From top
                if (i > 0) {
                    for (int balance : dp[i - 1][j])
                        possible.insert(balance);
                }

                // From left
                if (j > 0) {
                    for (int balance : dp[i][j - 1])
                        possible.insert(balance);
                }

                // Apply current parenthesis
                for (int balance : possible) {
                    int newBalance;

                    if (grid[i][j] == '(')
                        newBalance = balance + 1;
                    else
                        newBalance = balance - 1;

                    // Balance can never become negative
                    if (newBalance >= 0)
                        dp[i][j].insert(newBalance);
                }
            }
        }

        // Valid parentheses string must end with balance 0
        return dp[m - 1][n - 1].count(0) > 0;
    }
};