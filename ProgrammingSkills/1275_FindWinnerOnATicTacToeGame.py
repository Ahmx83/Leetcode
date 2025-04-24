class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = [[' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' '],]
        a_turn = True

        x_win = ['X', 'X', 'X']
        o_win = ['O', 'O', 'O']

        for x, y in moves:
            if a_turn:
                grid[x][y] = 'X'
            else:
                grid[x][y] = 'O'
            a_turn = True if a_turn is False else False

        for row in grid:
            if row == x_win:
                return 'A'
            if row == o_win:
                return 'B'

        for i in range(3):
            column = [grid[0][i], grid[1][i], grid[2][i]]
            if column == x_win:
                return 'A'
            if column == o_win:
                return 'B'

        diagonal1 = []
        diagonal2 = []
        for i in range(3):
            diagonal1.append(grid[i][i])
            diagonal2.append(grid[i][-i-1])

        if diagonal1 == x_win or diagonal2 == x_win:
            return 'A'
        elif diagonal1 == o_win or diagonal2 == o_win:
            return 'B'

        if len(moves) < 9:
            return 'Pending'
        return 'Draw'

sol = Solution()
# a = sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
# print(a)
b = sol.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
print(b)