from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)

        radiant = deque()
        dire = deque()

        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # Radiant senator bans Dire senator
                radiant.append(r + n)
            else:
                # Dire senator bans Radiant senator
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"