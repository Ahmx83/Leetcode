class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: list[list[int]]
        :rtype: List[int]
        """
        flattened = []

        def lap(mat):
            column = len(mat)
            try:
                # extend and pop the top row
                flattened.extend(mat[0])
                mat.pop(0)

                first_column = []

                for row in range(column-1):
                    # append and pop last column
                    flattened.append(mat[row][-1])
                    mat[row].pop(-1)
                    # print(flattened)

                    if len(mat[-1]) == 1:
                        continue

                    # prepare the first column
                    first_column.append(mat[row][0])
                    mat[row].pop(0)


                # extend and pop last row
                flattened.extend(reversed(mat[-1]))

                mat.pop(-1)
                # extend and pop first column
                flattened.extend(reversed(first_column))

            except IndexError:
                return False
            return True

        proceed = True
        while proceed:
            proceed = lap(matrix)
        return flattened


sol = Solution()
# a = sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# b = sol.spiralOrder([[7],[9],[6]])
# print(b)
# c = sol.spiralOrder([[1, 2, 3, 4 ],
#                      [5, 6, 7, 8 ],
#                      [9, 10,11,12],
#                      [13,14,15,16],
#                      [17,18,19,20],
#                      [21,22,23,24]])
# print(c)
# d = sol.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# print(d)