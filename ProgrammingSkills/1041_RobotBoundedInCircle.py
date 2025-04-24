class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        degree = 90
        coordinate = [0, 0]
        origin_point = coordinate[:]
        for i in range(4):

            for inst in instructions:
                if -360 >= degree or degree >= 360:
                    degree = degree % 360

                if inst == 'G':
                    # if it is facing north
                    if degree == 90 or degree == -270:
                        coordinate[1] += 1
                    # if it is facing south
                    elif degree == 270 or degree == -90:
                        coordinate[1] -= 1
                    # if it is facing east
                    elif degree == 0:
                        coordinate[0] += 1
                    elif degree == 180 or degree == -180:
                        coordinate[0] -= 1

                elif inst == 'L':
                    degree += 90
                elif inst == 'R':
                    degree -= 90
            if i == 0 and coordinate == origin_point:
                return True
        return coordinate == origin_point


sol = Solution()
a = sol.isRobotBounded('LLGRL')
print(a)