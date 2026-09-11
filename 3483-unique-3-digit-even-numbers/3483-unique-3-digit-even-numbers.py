class Solution:
    def totalNumbers(self, digits):
        count = 0

        # Frequency of each digit
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        # Check every 3-digit number
        for num in range(100, 1000, 2):  # only even numbers
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Use a temporary frequency
            used = [0] * 10
            used[a] += 1
            used[b] += 1
            used[c] += 1

            # Check if available in digits
            possible = True

            for d in range(10):
                if used[d] > freq[d]:
                    possible = False
                    break

            if possible:
                count += 1

        return count