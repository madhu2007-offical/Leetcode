class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Closest x-coordinate on the rectangle
        closest_x = max(x1, min(xCenter, x2))

        # Closest y-coordinate on the rectangle
        closest_y = max(y1, min(yCenter, y2))

        # Distance squared from circle center to closest rectangle point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        return dx * dx + dy * dy <= radius * radius