from src.Domain.board import Board


class Game:

    def __init__(self, board):
        """
        1- down
        2- up
        3- right
        4- left
        :param board:
        """
        self._board = board

    def find_snake_head(self):
        for i in range(0, self._board.dimension):
            for j in range(0, self._board.dimension):
                if self._board.board[i][j] == 2:
                    row = i
                    column = j
                    return row, column

    def check_where_is_the_body_of_the_snake(self, row, column):

        if self._board.board[row-1][column] == 3:
            return 1
        if self._board.board[row+1][column] == 3:
            return 2
        if self._board.board[row][column-1] == 3:
            return 3
        if self._board.board[row][column+1] == 3:
            return 4

    def check_for_game_over(self, row, column):
        if row - 1 == -1:
            return True
        if row + 1 == self._board.dimension:
            return True
        if column - 1 == -1:
            return True
        if column + 1 == self._board.dimension+1:
            return True

    def validate_move_left_1(self, row, column):
        if self._board.board[row][column-1] == 3:
            return True

    def validate_move_left_2(self, row, column):
        if self._board.board[row][column+1] == 3:
            return True

    def validate_move_left_3(self, row, column):
        if self._board.board[row+1][column] == 3:
            return True

    def validate_move_left_4(self, row, column):
        if self._board.board[row-1][column] == 3:
            return True

    def validate_move_right(self, row, column):
        if self._board.board[row][column+1] == 3:
            return True
    """
    def move_snake_to_left(self):
        row, column = self.find_snake_head()
        game_over = self.check_for_game_over(row, column)
        game_over_2 = self.validate_move_left_1(row, column)
        if game_over:
            return True
        if game_over_2:
            return True
        self._board.place_piece(row + 2, column, 0)
        self._board.place_piece(row, column, 3)
        self._board.place_piece(row, column - 1, 2)
    """

    def move_snake_to_left_2(self):
        row, column = self.find_snake_head()
        direction = self.check_where_is_the_body_of_the_snake(row, column)
        if direction == 2:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_1(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row + 2, column, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row, column - 1, 2)
        elif direction == 1:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_2(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row - 1, column + 1, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row, column + 1, 2)

        elif direction == 4:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_3(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row+1, column+1, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row+1, column, 2)

        elif direction == 3:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_4(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row-1, column-1, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row-1, column, 2)

    def move_snake_to_right_2(self):
        row, column = self.find_snake_head()
        direction = self.check_where_is_the_body_of_the_snake(row, column)
        if direction == 2:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_1(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row + 2, column, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row, column - 1, 2)

        elif direction == 1:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_2(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row - 1, column + 1, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row, column + 1, 2)

        elif direction == 4:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_3(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row+1, column+1, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row-1, column, 2)

        elif direction == 3:
            game_over = self.check_for_game_over(row, column)
            game_over_2 = self.validate_move_left_4(row, column)
            if game_over:
                return True
            if game_over_2:
                return True
            self._board.place_piece(row-1, column-1, 0)
            self._board.place_piece(row, column, 3)
            self._board.place_piece(row+1, column, 2)

    def move_snake_to_right(self):
        row, column = self.find_snake_head()
        game_over = self.check_for_game_over(row, column)
        game_over_2 = self.validate_move_right(row, column)
        if game_over:
            return True
        if game_over_2:
            return True
        self._board.place_piece(row + 2, column, 0)
        self._board.place_piece(row, column, 3)
        self._board.place_piece(row, column + 1, 2)

    def move_snake_with_move_command(self, params):
        row, column = self.find_snake_head()
        direction = self.check_where_is_the_body_of_the_snake(row, column)
        if direction == 1:
            while params > 0:
                game_over = self.check_for_game_over(row, column)
                if game_over:
                    return True
                self._board.place_piece(row-2, column, 0)
                self._board.place_piece(row, column, 3)
                self._board.place_piece(row+1, column, 2)
                params = params - 1
                row, column = self.find_snake_head()
            return False

        elif direction == 2:
            while params > 0:
                game_over = self.check_for_game_over(row, column)
                if game_over:
                    return True
                self._board.place_piece(row+2, column, 0)
                self._board.place_piece(row, column, 3)
                self._board.place_piece(row-1, column, 2)
                params = params - 1
                row, column = self.find_snake_head()
            return False
        elif direction == 3:
            while params > 0:
                game_over = self.check_for_game_over(row, column)
                if game_over:
                    return True
                self._board.place_piece(row + 2, column, 0)
                self._board.place_piece(row, column, 3)
                self._board.place_piece(row, column + 1, 2)
                params = params - 1
                row, column = self.find_snake_head()

        elif direction == 4:
            while params > 0:
                game_over = self.check_for_game_over(row, column)
                if game_over:
                    return True
                self._board.place_piece(row + 2, column, 0)
                self._board.place_piece(row, column, 3)
                self._board.place_piece(row, column - 1, 2)
                params = params - 1
                row, column = self.find_snake_head()

    def split_command(self, command):
        """
        With this function we split a command and some parameters
        :param command: the command we want to split
        :return: it will return the command and the parameters in two different variables
        """
        tokens = command.strip().split(' ', 1)
        tokens[0] = tokens[0].strip().lower()
        return tokens[0], '' if len(tokens) == 1 else tokens[1].strip()


    def clear_snake_from_board(self):
        pass
