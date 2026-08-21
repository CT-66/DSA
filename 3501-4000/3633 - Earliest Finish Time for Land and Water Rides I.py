class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        
        ans = float('inf')

        # Land first, then water
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_finish = max(land_finish, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, water_finish)

        # Water first, then land
        for i in range(len(waterStartTime)):
            water_finish = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):
                land_finish = max(water_finish, landStartTime[j]) + landDuration[j]
                ans = min(ans, land_finish)

        return ans