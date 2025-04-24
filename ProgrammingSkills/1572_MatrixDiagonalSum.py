class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: list[list[int]]
        :rtype: int
        """
        total = []
        mat_len = len(mat)
        # if diagonals don't have the same center
        if mat_len % 2 == 0:
            for i in range(mat_len):
                total.append(mat[i][i])
                total.append(mat[i][-i - 1])
        # if diagonals have the same center
        else:
            for i in range(mat_len):
                total.append(mat[i][i])
                if i != mat_len // 2:
                    total.append(mat[i][-i - 1])

        return sum(total)
