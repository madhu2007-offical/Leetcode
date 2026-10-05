class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Length must be the same
        if len(word1) != len(word2):
            return False

        # Count characters
        count1 = {}
        count2 = {}

        for ch in word1:
            count1[ch] = count1.get(ch, 0) + 1

        for ch in word2:
            count2[ch] = count2.get(ch, 0) + 1

        # Both strings must contain the same characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Frequency distributions must be the same
        return sorted(count1.values()) == sorted(count2.values())