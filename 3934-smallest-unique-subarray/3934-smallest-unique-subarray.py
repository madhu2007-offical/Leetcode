from collections import Counter


class Solution:

  def smallestUniqueSubarray(self, nums):
    n = len(nums)

    # Fast check for length 1
    counts = Counter(nums)
    if any(v == 1 for v in counts.values()):
      return 1

    # Double rolling hash constants
    MOD1, BASE1 = 10**9 + 7, 1315423911
    MOD2, BASE2 = 10**9 + 9, 2654435761

    def has_unique(length):
      h1, h2 = 0, 0
      p1 = pow(BASE1, length - 1, MOD1)
      p2 = pow(BASE2, length - 1, MOD2)

      # Initial window [0 ... length - 1]
      for i in range(length):
        h1 = (h1 * BASE1 + nums[i]) % MOD1
        h2 = (h2 * BASE2 + nums[i]) % MOD2

      freq = {(h1, h2): 1}

      # Slide the window across the array
      for i in range(length, n):
        # Remove leftmost element
        h1 = (h1 - nums[i - length] * p1) % MOD1
        h2 = (h2 - nums[i - length] * p2) % MOD2

        # Add new rightmost element
        h1 = (h1 * BASE1 + nums[i]) % MOD1
        h2 = (h2 * BASE2 + nums[i]) % MOD2

        state = (h1, h2)
        freq[state] = freq.get(state, 0) + 1

      return any(count == 1 for count in freq.values())

    low, high = 2, n
    ans = n

    while low <= high:
      mid = (low + high) // 2
      if has_unique(mid):
        ans = mid
        high = mid - 1
      else:
        low = mid + 1

    return ans