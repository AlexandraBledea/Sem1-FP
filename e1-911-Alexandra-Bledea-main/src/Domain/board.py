import random
import texttable
"""
-1 - mar
0 - nimic
2 - cap sarpe
3 - corp sarpe

"""


class GameException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class Board:

    def __init__(self, dimension, n_apples):
        self._dimension = dimension
        self._apples = n_apples
        self._board = [[0 for col in range(0, self._dimension+1)] for row in range(0, self._dimension)]
        self.place_snake()
        self.place_apples()

    @property
    def board(self):
        return self._board

    def place_piece(self, row, column, piece):
        self._board[row][column] = piece

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value

    @property
    def apples(self):
        return self._apples

    @apples.setter
    def apples(self, value):
        self._apples = value

    def create_board(self):
        self._board = [[0 for col in range(self._dimension)] for row in range(self._dimension)]

    def place_apples(self):
        spaces = []
        for i in range(0, self._dimension):
            for j in range(0, self._dimension):
                if self._board[i][j] == 0:
                    spaces.append([i, j])

        apples = self._apples
        while apples > 0:
            place = random.choice(spaces)
            row = place[0]
            column = place[1]
            spaces.remove(place)
            if self.check_not_adjacent(row, column):
                self._board[row][column] = -1
                apples = apples - 1

    def check_not_adjacent(self, row, column):
        if row == 0 and column == 0:
            if self._board[row+1][column] == 0 and self._board[row][column+1] == 0:
                return True
        if row == 0 and column == self._dimension - 1:
            if self._board[row][column-1] == 0 and self._board[row+1][column] == 0:
                return True

        if row == self._dimension - 1 and column == self._dimension - 1:
            if self._board[row][column-1] == 0 and self._board[row-1][column] == 0:
                return True

        if row == self._dimension - 1 and column == 0:
            if self._board[row-1][column] == 0 and self._board[row][column+1] == 0:
                return True

        if row == 0 and column != 0 and column != self._dimension - 1:
            if self._board[row][column-1] == 0 and self._board[row+1][column] == 0 and self._board[row][column+1] == 0:
                return True
        if row != 0 and column == 0 and row != self._dimension - 1:
            if self._board[row][column+1] == 0 and self._board[row+1][column] == 0 and self._board[row-1][column] == 0:
                return True
        if row != 0 and column != 0 and row != self._dimension - 1 and column != self._dimension - 1:
            if self._board[row][column + 1] == 0 and self._board[row][column-1] == 0 and \
                    self._board[row+1][column] == 0 and self. _board[row-1][column] == 0:
                return True
        return False

    def place_snake(self):
        middle = self._dimension//2
        self._board[middle-1][middle] = 2
        self._board[middle][middle] = 3
        self._board[middle+1][middle] = 3

    def __str__(self):
        t = texttable.Texttable()
        for row in range(0, self._dimension):
            data = []
            for val in self._board[row][0:-1]:
                if val == -1:
                    data.append(".")
                if val == 0:
                    data.append("")
                if val == 2:
                    data.append("*")
                if val == 3:
                    data.append("+")
            t.add_row(data)

        return t.draw()
