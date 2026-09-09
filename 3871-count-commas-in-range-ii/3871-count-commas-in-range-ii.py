class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_commas = 0
        threshold = 1000

        while n >= threshold:
            total_commas += n - threshold + 1
            threshold *= 1000

        return total_commas