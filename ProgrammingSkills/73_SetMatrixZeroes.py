class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: list[list[int]]
        :rtype: None
        """

        zero_columns = []
        zero_rows = []

        num_of_columns = len(matrix[0])
        num_of_rows = len(matrix)

        for nth_row, row in enumerate(matrix):
            for nth_column, unit in enumerate(row):
                if unit == 0:
                   zero_rows.append(nth_row)
                   zero_columns.append(nth_column)


        for i in range(num_of_rows):
            for j in zero_columns:
                matrix[i][j] = 0

        for j in zero_rows:
            matrix[j] = [0] * num_of_columns
