
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        q = sorted(enumerate(queries), key=lambda a: a[1])

        count = [0] * (n + 1)
        ans = [0] * len(queries)
        left = right = active = 0

        for idx, t in q:
            while right < len(logs) and logs[right][1] <= t:
                server = logs[right][0]
                if count[server] == 0:
                    active += 1
                count[server] += 1
                right += 1

            while left < right and logs[left][1] < t - x:
                server = logs[left][0]
                count[server] -= 1
                if count[server] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans
