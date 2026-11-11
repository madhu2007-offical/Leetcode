class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        both = min(need1, need2)

        ans = both * min(costBoth, cost1 + cost2)

        ans += (need1 - both) * min(cost1, costBoth)
        ans += (need2 - both) * min(cost2, costBoth)

        return ans