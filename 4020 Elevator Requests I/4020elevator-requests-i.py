class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        current = 0
        time = 0

        for floor in requests:
            time += abs(current - floor)
            current = floor

        return time