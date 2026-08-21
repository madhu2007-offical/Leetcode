from math import gcd


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:

        n = len(coins)

        # Remove redundant coins.
        # If a coin is a multiple of another coin,
        # its multiples are already covered.
        coins.sort()

        useful = []

        for c in coins:
            redundant = False

            for d in useful:
                if c % d == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(c)

        coins = useful
        n = len(coins)

        # Count distinct amounts <= x
        def count(x):
            total = 0

            for mask in range(1, 1 << n):

                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = (lcm // g) * coins[i]

                        # No need to continue if LCM > x
                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                ways = x // lcm

                if bits % 2 == 1:
                    total += ways
                else:
                    total -= ways

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left