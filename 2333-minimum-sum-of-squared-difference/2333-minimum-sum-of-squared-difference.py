
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        def operations_needed(level):
            return sum(max(0, d - level) for d in diffs)

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            if operations_needed(mid) <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        remaining = k - operations_needed(level)

        ans = 0

        for d in diffs:
            reduced = min(d, level)
            ans += reduced * reduced

        # Use remaining operations to reduce some values
        # that are currently equal to level by one.
        ans -= remaining * (2 * level - 1)

        return ans
