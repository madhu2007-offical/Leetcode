class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        left = 0
        ones = 0
        best = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Shrink until exactly k ones
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                # Remove leading zeros while keeping k ones
                temp_left = left
                while temp_left <= right and s[temp_left] == '0':
                    temp_left += 1

                curr = s[temp_left:right + 1]

                if not best or len(curr) < len(best) or \
                   (len(curr) == len(best) and curr < best):
                    best = curr

        return best