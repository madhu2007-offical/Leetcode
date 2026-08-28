class Solution(object):

    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check whether a palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Counts for the left half
        half_cnt = [x // 2 for x in cnt]
        m = n // 2

        def build(left):
            left = ''.join(left)

            if n % 2:
                return left + middle + left[::-1]

            return left + left[::-1]

        # --------------------------------------------------
        # Find the smallest permutation of the half that is
        # >= target[:m].
        # --------------------------------------------------

        target_half = target[:m]

        # First try to construct exactly target_half.
        # While doing this, remember positions where we
        # could instead choose a slightly larger character.
        remaining = half_cnt[:]
        prefix = []
        choices = []

        possible_equal = True

        for i in range(m):
            t = ord(target_half[i]) - ord('a')

            # We can choose a character > target[i].
            greater = -1

            for c in range(t + 1, 26):
                if remaining[c] > 0:
                    greater = c
                    break

            # Save this position as a possible place to
            # make the palindrome greater.
            if greater != -1:
                choices.append((i, prefix[:], greater, remaining[:]))

            # Try to stay equal to target
            if remaining[t] > 0:
                prefix.append(chr(t + ord('a')))
                remaining[t] -= 1
            else:
                possible_equal = False
                break

        # --------------------------------------------------
        # Case 1:
        # target_half itself can be formed.
        # --------------------------------------------------

        if possible_equal:
            candidate = build(prefix)

            if candidate > target:
                return candidate

        # --------------------------------------------------
        # Case 2:
        # Make the smallest possible increase at the
        # RIGHTMOST useful position.
        #
        # Rightmost is important because it keeps the result
        # lexicographically smallest.
        # --------------------------------------------------

        for i, old_prefix, greater, rem in reversed(choices):

            new_left = old_prefix[:]

            # Put the smallest character greater than target[i]
            new_left.append(chr(greater + ord('a')))
            rem[greater] -= 1

            # Fill everything after i with smallest characters
            for c in range(26):
                if rem[c] > 0:
                    new_left.extend(
                        [chr(c + ord('a'))] * rem[c]
                    )

            candidate = build(new_left)

            if candidate > target:
                return candidate

        return ""