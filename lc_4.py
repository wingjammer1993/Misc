class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heat_map = {}
        max_val = 0
        for idx, i in enumerate(heaters):
            for j in houses:
                if j not in heat_map:
                    heat_map[j] = abs(i - j)
                else:
                    heat_map[j] = min(heat_map[j], abs(i - j))
                if idx == len(heaters)-1:
                    if heat_map[j] > max_val:
                        max_val = heat_map[j]

        return max_val



a = []

s = Solution()
print(s.findRadius(a, b))


