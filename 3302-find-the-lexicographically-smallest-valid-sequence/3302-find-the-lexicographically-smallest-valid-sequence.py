import bisect

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # Store positions of each character in word1
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(word1):
            pos[ord(ch) - ord('a')].append(i)

        # last0[j]: max index in word1 to match word2[j...m-1] with 0 mismatches
        last0 = [-1] * m
        curr = n - 1
        for j in range(m - 1, -1, -1):
            target = ord(word2[j]) - ord('a')
            idx = bisect.bisect_right(pos[target], curr) - 1
            if idx >= 0:
                last0[j] = pos[target][idx]
                curr = last0[j] - 1
            else:
                break

        # last1[j]: max index in word1 to match word2[j...m-1] with at most 1 mismatch
        last1 = [-1] * m
        for j in range(m - 1, -1, -1):
            # Option 1: Mismatch at j
            opt1 = (n - 1) if j == m - 1 else (last0[j + 1] - 1 if last0[j + 1] != -1 else -1)

            # Option 2: Exact match at j
            limit = n if j == m - 1 else last1[j + 1]
            target = ord(word2[j]) - ord('a')
            idx = bisect.bisect_left(pos[target], limit) - 1
            opt2 = pos[target][idx] if idx >= 0 else -1

            last1[j] = max(opt1, opt2)

        # Step 3: Greedy construction of the result sequence
        seq = []
        i = 0
        used_mismatch = False

        for j in range(m):
            found = False
            while i < n:
                if used_mismatch:
                    # Must match exactly and remaining suffix must match with 0 mismatches
                    if word1[i] == word2[j]:
                        if j + 1 == m or last0[j + 1] > i:
                            seq.append(i)
                            i += 1
                            found = True
                            break
                else:
                    if word1[i] == word2[j]:
                        # Exact match at j, suffix needs at most 1 mismatch
                        if j + 1 == m or last1[j + 1] > i:
                            seq.append(i)
                            i += 1
                            found = True
                            break
                    else:
                        # Mismatch at j, suffix needs 0 mismatches
                        if j + 1 == m or last0[j + 1] > i:
                            seq.append(i)
                            used_mismatch = True
                            i += 1
                            found = True
                            break
                i += 1

            if not found:
                return []

        return seq