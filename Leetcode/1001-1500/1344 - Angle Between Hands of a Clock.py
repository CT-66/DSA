class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Formula: 11/2 M - 30 H
        # if minutes == hour:
            # return 0
        angle = abs(((11/2) * minutes ) - (30 * hour))
        if angle >= 180:
            return 360 - angle
        return angle