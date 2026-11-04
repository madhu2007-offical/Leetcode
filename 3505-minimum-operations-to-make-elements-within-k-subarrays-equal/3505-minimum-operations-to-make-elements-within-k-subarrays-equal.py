import heapq
from collections import defaultdict

class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)
        lo, hi = [], []              # lo: max-heap (negated), hi: min-heap
        delayed = defaultdict(int)   # lazy deletions
        s = [0, 0, 0, 0]             # lo_size, hi_size, lo_sum, hi_sum

        def prune_lo():
            while lo and delayed[-lo[0]] > 0:
                delayed[-lo[0]] -= 1
                heapq.heappop(lo)

        def prune_hi():
            while hi and delayed[hi[0]] > 0:
                delayed[hi[0]] -= 1
                heapq.heappop(hi)

        def rebalance():
            if s[0] > s[1] + 1:
                v = -heapq.heappop(lo)
                s[0] -= 1
                s[2] -= v
                heapq.heappush(hi, v)
                s[1] += 1
                s[3] += v
                prune_lo()
            elif s[0] < s[1]:
                v = heapq.heappop(hi)
                s[1] -= 1
                s[3] -= v
                heapq.heappush(lo, -v)
                s[0] += 1
                s[2] += v
                prune_hi()

        def add(v):
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v)
                s[0] += 1
                s[2] += v
            else:
                heapq.heappush(hi, v)
                s[1] += 1
                s[3] += v
            rebalance()

        def remove(v):
            delayed[v] += 1
            if v <= -lo[0]:
                s[0] -= 1
                s[2] -= v
                if v == -lo[0]:
                    prune_lo()
            else:
                s[1] -= 1
                s[3] -= v
                if hi and v == hi[0]:
                    prune_hi()
            rebalance()

        m = n - x + 1
        cost = [0] * m
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                med = -lo[0]
                cost[i - x + 1] = (med * s[0] - s[2]) + (s[3] - med * s[1])

        INF = float('inf')
        prev = [0] * (n + 1)         # dp[0][*] = 0
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]