class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        groups = [[] for _ in range(1501)]

        for i in range(n):
            p = items[i][1]
            groups[p].append(1 + free[i])

        dp = [-1] * (budget + 1)
        dp[0] = 0

        ans = 0
        neg = -10**9

        for p in range(1500, 0, -1):
            if not groups[p]:
                continue

            exact = [neg] * (budget + 1)

            for val in groups[p]:
                for c in range(budget, p - 1, -1):
                    exact[c] = max(
                        exact[c],
                        exact[c - p] + val,
                        dp[c - p] + val
                    )

            for c in range(budget + 1):
                if exact[c] != neg:
                    ans = max(ans, exact[c] + (budget - c) // p)

            for val in groups[p]:
                for c in range(budget, p - 1, -1):
                    dp[c] = max(dp[c], dp[c - p] + val)

        return ans