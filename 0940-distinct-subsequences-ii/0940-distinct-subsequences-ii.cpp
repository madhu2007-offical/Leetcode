class Solution {
public:
    int distinctSubseqII(string s) {
        const int MOD = 1e9 + 7;

        vector<long long> dp(26, 0);
        long long total = 0;

        for (char c : s) {
            int i = c - 'a';

            long long newSubseq = (total + 1) % MOD;

            total = (total + newSubseq - dp[i] + MOD) % MOD;

            dp[i] = newSubseq;
        }

        return total;
    }
};