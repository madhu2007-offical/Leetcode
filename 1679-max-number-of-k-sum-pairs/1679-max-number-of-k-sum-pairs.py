class Solution:
    def maxOperations(self, nums, k):
        count = {}
        operations = 0

        for num in nums:
            complement = k - num

            if count.get(complement, 0) > 0:
                operations += 1
                count[complement] -= 1
            else:
                count[num] = count.get(num, 0) + 1

        return operations