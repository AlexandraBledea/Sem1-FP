import numpy as np


class GameException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class Board:

    def __init__(self):
        """
        Here we initialize our board with 6 rows and 7 columns which contains the value 0
        The value 0 meaning that space is available on the board
        """
        self._number_of_rows = 6
        self._number_of_columns = 7
        self._board = np.zeros((self._number_of_rows, self._number_of_columns))

    @property
    def number_of_rows(self):
        """
        :return: the number of rows
        """
        return self._number_of_rows

    @property
    def number_of_columns(self):
        """
        :return: the number of columns
        """
        return self._number_of_columns

    @property
    def board(self):
        """
        :return: the board
        """
        return self._board

    def check_availability(self, row, column):
        """
        With this function we check if a specified position on the board is available
        :param row: the row for which we want to check
        :param column: the column for which we want to check
        :return: returns true if the position is available and false if not
        """
        return self._board[row][column] == 0

    def is_free(self, column):
        """
        With this function we check if there is an available position on the last row
        :param column: the column for which we want to checl
        :return: returns true if the position is available and false if not
        """
        return self._board[self._number_of_rows - 1][column] == 0

    def get_new_open_row(self, column):
        """
        With this function, for a specified column we get a new row for which the position is available and checks
        all the conditions
        :param column: the column for which we want to get the new available row
        :return: the available row
        """
        for row in range(self._number_of_rows):
            if self._board[row][column] == 0:
                return row

    def place_piece(self, row, column, piece):
        """
        With this function we place a piece on the board at a specified position
        :param row: the row for which we want the piece to be placed
        :param column: the column for which we want the piece to be placed
        :param piece: the piece we want to place
        :return: it doesn't return anything
        """
        self._board[row][column] = piece

    def print_board(self):
        """
        With this function we print the board in a reverse order
        :return: it doesn't return anything
        """
        print(np.flip(self._board, 0))
