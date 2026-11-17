class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        
        # Precompute proper divisors for every possible substring length L (2 <= L <= n)
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divisors[L].append(d)
                    
        # Helper to compute min changes to make s[i..j] a semi-palindrome
        def get_cost(i, j):
            L = j - i + 1
            min_changes = L  # Upper bound
            
            for d in divisors[L]:
                changes = 0
                # Check each of the d interleaved groups
                for r in range(d):
                    left = i + r
                    right = j - (d - 1 - r)
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                if changes < min_changes:
                    min_changes = changes
                    if min_changes == 0:
                        break
            return min_changes

        # 1. Precompute cost[i][j] for all valid substrings (length >= 2)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(i, j)
                
        # 2. DP to partition s[0..i-1] into p semi-palindromes
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            # Minimum end index i requires at least 2*p characters
            # Maximum end index i must leave at least 2*(k - p) characters for remaining parts
            min_i = 2 * p
            max_i = n - 2 * (k - p)
            for i in range(min_i, max_i + 1):
                for j in range(2 * (p - 1), i - 1):
                    if dp[p - 1][j] + cost[j][i - 1] < dp[p][i]:
                        dp[p][i] = dp[p - 1][j] + cost[j][i - 1]
                        
        return dp[k][n]