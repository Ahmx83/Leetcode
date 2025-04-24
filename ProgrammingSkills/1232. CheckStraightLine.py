class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: list[list[int]]
        :rtype: bool
        """

        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x3, y3 in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
        return True
sol = Solution()
# a = sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
# print(a)
# b = sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
# print(b)
# c = sol.checkStraightLine([[0,0],[0,1],[0,-1]])
# print(c)
# d = sol.checkStraightLine([[0,0],[0,5],[5,5],[5,0]])
# print(d)
e = sol.checkStraightLine([[0,1],[1,3],[-4,-7],[5,11]])
print(e)