class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: list[str | int]
        :rtype: int
        """
        scores = []
        for i in operations:
            if i == '+':
                scores.append(scores[-1] + scores[-2])
            elif i == 'D':
                scores.append(scores[-1] * 2)
            elif i == 'C':
                scores.pop()
            else:
                scores.append(int(i))
        return sum(scores)


a = Solution()
b = a.calPoints([1, 2, 3, "D"])
# print(b)
c = a.calPoints(["5","2","C","D","+"])

