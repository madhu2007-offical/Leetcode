class Solution(object):

    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """

        def is_prime(x):
            if x < 2:
                return False

            if x % 2 == 0:
                return x == 2

            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2

            return True

        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        half = 10

        while True:
            s = str(half)

            # Create odd-length palindrome
            palindrome = int(s + s[-2::-1])

            if palindrome >= n and is_prime(palindrome):
                return palindrome

            half += 1