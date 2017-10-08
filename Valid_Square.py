import math


class Solution:

    def get_slope(self, point1, point2):
        if 0 == point2[0] - point1[0]:
            slope = float('inf')
            return slope
        if 0 == point2[-1] - point1[-1]:
            slope = 0
            return slope
        else:
            slope = float((point2[-1] - point1[-1])) / float((point2[0] - point1[0]))
            return slope

    def is_perpendicular(self, ref, point1, point2):
        infinity = float('inf')
        slope1 = self.get_slope(ref, point1)
        slope2 = self.get_slope(ref, point2)
        if infinity == slope1 or infinity == slope2:
            if 0 == slope1 or 0 == slope2:
                return True
            else:
                return False

        else:
            product = slope1*slope2

            if -1 == round(product, 2):
                return 1
            else:
                return 0

    def distance(self, point1, point2):
        d1 = point2[-1] - point1[-1]
        d2 = point2[0] - point1[0]
        distance = math.pow(d1, 2) + math.pow(d2, 2)
        distance = math.sqrt(distance)
        distance = math.fabs(distance)
        return distance

    def validSquare(self, p1, p2, p3, p4):
        d2 = self.distance(p1, p2)
        d3 = self.distance(p1, p3)
        d4 = self.distance(p1, p4)

        if d2 == d3:
            perp11 = self.is_perpendicular(p1, p2, p3)
            perp22 = self.is_perpendicular(p4, p2, p3)
            if perp11 and perp22:
                return True
            else:
                return False

        if d2 == d4:
            perp33 = self.is_perpendicular(p1, p2, p4)
            perp44 = self.is_perpendicular(p3, p2, p4)
            if perp33 and perp44:
                return True
            else:
                return False

        if d3 == d4:
            perp55 = self.is_perpendicular(p1, p3, p4)
            perp66 = self.is_perpendicular(p2, p3, p4)
            if perp55 and perp66:
                return True
            else:
                return False

        else:
            return False







if __name__ == "__main__":

    s = Solution()
    p1 = [-658,-2922]
    p2 = [-965,-4209]
    p3 = [-2252,-3902]
    p4 = [-1945,-2615]
    answer = s.validSquare(p1, p2, p3, p4)
    print(answer)







