class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        minDist = float('inf')
        minDrone = -1
        for i in drones:
            # print(i)
            x = i[0]
            y = i[1]
            # print(x, y)
            dist = abs(x - target[0]) + abs(y - target[1])
            if dist <= i[2] and dist < minDist:
                # minDist = min(minDist, dist)
                # if drones.index(i) == minDrone:
                #     break
                minDist = dist
                minDrone = drones.index(i)
            # else:
            #     minDrone = -1
        # return dist
        return minDrone