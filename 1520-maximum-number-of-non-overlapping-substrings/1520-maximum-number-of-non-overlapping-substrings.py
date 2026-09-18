class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Find the smallest valid interval starting
        # from the first occurrence of each character
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character occurs before our interval
                if first[x] < left:
                    valid = False
                    break

                # Extend interval to include all occurrences
                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        # Choose maximum number of non-overlapping intervals.
        # Earlier ending interval is preferred.
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result