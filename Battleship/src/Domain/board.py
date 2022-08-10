import texttable


class GameException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class Board:

    def __init__(self):
        self._columns = 6
        self._rows = 6
        self._player_board = [[0 for col in range(self._columns + 2)] for row in range(self._rows + 2)]
        self._enemy_board = [[0 for col in range(self._columns + 2)] for row in range(self._rows + 2)]

    @property
    def player_board(self):
        return self._player_board

    @property
    def enemy_board(self):
        return self._enemy_board

    @property
    def columns(self):
        return self._columns

    @property
    def rows(self):
        return self._rows

    def place_piece_player(self, row, column, piece):
        self._player_board[row][column] = piece

    def place_piece_enemy(self, row, column, piece):
        self._enemy_board[row][column] = piece

    def is_free_player(self, row, column):
        return self._player_board[row][column] == 0

    def is_free_enemy(self, row, column):
        return self._enemy_board[row][column] == 0

