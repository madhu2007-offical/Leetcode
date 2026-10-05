class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        occurrences = list(count.values())

        return len(occurrences) == len(set(occurrences))