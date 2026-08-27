class Solution(object):

    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        # Frequency of characters in s
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(s)

        # Store the frequency array BEFORE using target[i]
        snapshots = []

        # Try to match target from left to right
        for i in range(n):

            snapshots.append(cnt[:])

            t = ord(target[i]) - ord('a')

            # First priority: match target[i]
            if cnt[t] > 0:
                cnt[t] -= 1
                continue

            # Cannot match target[i].
            # Try the smallest character greater than target[i].
            for c in range(t + 1, 26):

                if cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))

                    # Put remaining characters in sorted order
                    for x in range(26):
                        ans += chr(x + ord('a')) * cnt[x]

                    return ans

            # Neither equal nor greater is possible.
            break

        # Backtrack.
        # Try increasing the rightmost possible position.
        for i in range(len(snapshots) - 1, -1, -1):

            cnt = snapshots[i]

            t = ord(target[i]) - ord('a')

            # Find the smallest available character > target[i]
            for c in range(t + 1, 26):

                if cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))

                    # Smallest possible suffix
                    for x in range(26):
                        ans += chr(x + ord('a')) * cnt[x]

                    return ans

        return ""