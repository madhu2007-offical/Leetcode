class Solution:
    def checkDivisibility(self, n):
        original_n = n
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n //= 10

        return original_n % (digit_sum + digit_product) == 0