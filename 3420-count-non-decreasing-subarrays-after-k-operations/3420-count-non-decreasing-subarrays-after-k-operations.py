from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()
        cost = 0
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            x = nums[l]
            cnt = 1

            while dq and dq[-1][0] < x:
                v, c = dq.pop()
                cost += (x - v) * c
                cnt += c

            dq.append((x, cnt))

            while cost > k:
                v, c = dq[0]
                cost -= v - nums[r]
                r -= 1

                if c == 1:
                    dq.popleft()
                else:
                    dq[0] = (v, c - 1)

            ans += r - l + 1

        return ans