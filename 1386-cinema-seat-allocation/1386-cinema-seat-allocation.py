class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats: 
            rows.setdefault(row, set()).add(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = not any(s in seats for s in [2,3,4,5])
            middle = not any(s in seats for s in [4,5,6,7])
            right = not any(s in seats for s in [6,7,8,9])

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans




        