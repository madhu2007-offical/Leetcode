class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        start = 0

        for end in range(1, n + 1):
            # End the current group if there is a gap > limit
            if end == n or arr[end][0] - arr[end - 1][0] > limit:

                # Values in this group
                values = [arr[i][0] for i in range(start, end)]

                # Original indices in this group
                indices = [arr[i][1] for i in range(start, end)]

                # Put smallest values at smallest indices
                indices.sort()

                for idx, value in zip(indices, values):
                    ans[idx] = value

                start = end

        return ans