class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        end_point = [0, 0]
        end_point[0] += moves.count("R")
        end_point[0] -= moves.count("L")
        end_point[1] += moves.count("U")
        end_point[1] -= moves.count("D")

        return end_point == [0, 0]