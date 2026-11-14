class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            s = 0
            for j in range(i, min(n, i + r)):
                s += nums[j]

                length = j - i + 1
                if l <= length <= r and s > 0:
                    ans = min(ans, s)

        return ans if ans != float('inf') else -1