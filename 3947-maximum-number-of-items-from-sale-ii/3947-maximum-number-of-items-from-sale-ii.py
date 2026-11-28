
class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)

        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1

        capacity = [0] * (n + 1)

        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                capacity[f] += cnt[j]
            capacity[f] -= 1

        min_price = min(p for f, p in items)

        items.sort(key=lambda x: x[1])

        ans = 0

        for f, p in items:
            if p >= 2 * min_price:
                break

            if budget < p:
                break

            buy = min(capacity[f], budget // p)

            ans += 2 * buy
            budget -= buy * p

        ans += budget // min_price

        return ans
