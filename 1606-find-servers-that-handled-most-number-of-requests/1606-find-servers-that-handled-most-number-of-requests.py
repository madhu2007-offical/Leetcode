
from heapq import heappush, heappop

class Solution:
    def busiestServers(self, k, arrival, load):
        bit = [0] * (k + 1)

        def update(i, delta):
            i += 1
            while i <= k:
                bit[i] += delta
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def find(target):
            pos = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = pos + step
                if nxt <= k and bit[nxt] < target:
                    target -= bit[nxt]
                    pos = nxt
                step >>= 1

            return pos

        for i in range(k):
            update(i, 1)

        busy = []
        count = [0] * k

        for i, (t, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, server = heappop(busy)
                update(server, 1)

            total = query(k)

            if total == 0:
                continue

            start = i % k
            before = query(start)

            if total > before:
                server = find(before + 1)
            else:
                server = find(1)

            update(server, -1)
            count[server] += 1
            heappush(busy, (t + duration, server))

        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum]
