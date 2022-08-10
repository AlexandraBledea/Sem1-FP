import random


class RandomStrategy:

    def __init__(self, board):
        self._board = board

    def validate_place(self, row, column):
        """
        With this function we check whether the computer places its piece on a valid place
        A valid place meaning for example if he want to place its piece on the column 2 on the row 3, then on the same
        column but on the row 2, 1 and 0 should already be placed a piece
        :param row: the row for which we validate the place
        :param column: the column for which we validate the place
        :return: it returns true if the place is valid and false if not
        """
        ok = 0
        check_value = row
        if row == 0 and self._board.board[row][column] == 0:
            return True
        row = row - 1
        while row >= 0:
            if row == 0:
                if self._board.board[row][column] != 0:
                    ok = ok + 1
            elif row == 1:
                if self._board.board[row][column] != 0:
                    ok = ok + 1
            elif row == 2:
                if self._board.board[row][column] != 0:
                    ok = ok + 1
            elif row == 3:
                if self._board.board[row][column] != 0:
                    ok = ok + 1
            elif row == 4:
                if self._board.board[row][column] != 0:
                    ok = ok + 1
            elif row == 5:
                if self._board.board[row][column] != 0:
                    ok = ok + 1
            row = row - 1
        if ok == check_value:
            return True
        else:
            return False

    def block_enemy(self, first_piece, second_piece):
        """
        With this function we check whether the computer can block the enemy from winning the game, when he is one move
        away, and if it can then it places the piece there
        :param first_piece: human player's piece
        :param second_piece: computer's piece
        :return: it returns true if the computer can block the enemy and false if not
        """

        a_move_was_made = False

        # We check if the enemy can block the enemy on a row
        for column in range(self._board.number_of_columns - 3):
            for row in range(self._board.number_of_rows):
                if self._board.board[row][column] == first_piece and\
                        self._board.board[row][column + 1] == first_piece and \
                        self._board.board[row][column + 2] == first_piece:
                    if self._board.check_availability(row, column + 3):
                        if self.validate_place(row, column + 3):
                            self._board.place_piece(row, column + 3, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == first_piece and \
                        self._board.board[row][column + 1] == first_piece and \
                        self._board.board[row][column + 3] == first_piece:
                    if self._board.check_availability(row, column + 2):
                        if self.validate_place(row, column + 2):
                            self._board.place_piece(row, column + 2, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == first_piece and \
                        self._board.board[row][column + 2] == first_piece and \
                        self._board.board[row][column + 3] == first_piece:
                    if self._board.check_availability(row, column + 1):
                        if self.validate_place(row, column + 1):
                            self._board.place_piece(row, column + 1, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column + 1] == first_piece and \
                        self._board.board[row][column + 2] == first_piece and \
                        self._board.board[row][column + 3] == first_piece:
                    if self._board.check_availability(row, column):
                        if self.validate_place(row, column):
                            self._board.place_piece(row, column, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

        # We check if the computer can block the enemy on a column
        for column in range(self._board.number_of_columns):
            for row in range(self._board.number_of_rows - 3):
                if self._board.board[row][column] == first_piece and\
                        self._board.board[row + 1][column] == first_piece and \
                        self._board.board[row + 2][column] == first_piece:
                    if self._board.check_availability(row + 3, column):
                        self._board.place_piece(row + 3, column, second_piece)
                        a_move_was_made = True
                        return a_move_was_made

        # We check if the computer can block the enemy on a positive diagonal
        for column in range(self._board.number_of_columns - 3):
            for row in range(self._board.number_of_rows - 3):
                if self._board.board[row][column] == first_piece and \
                        self._board.board[row + 1][column + 1] == first_piece and \
                        self._board.board[row + 2][column + 2] == first_piece:
                    if self._board.check_availability(row + 3, column + 3):
                        if self.validate_place(row + 3, column + 3):
                            self._board.place_piece(row + 3, column + 3, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == first_piece and \
                        self._board.board[row + 1][column + 1] == first_piece and \
                        self._board.board[row + 3][column + 3] == first_piece:
                    if self._board.check_availability(row + 2, column + 2):
                        if self.validate_place(row + 2, column + 2):
                            self._board.place_piece(row + 2, column + 2, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == first_piece and \
                        self._board.board[row + 2][column + 2] == first_piece and \
                        self._board.board[row + 3][column + 3] == first_piece:
                    if self._board.check_availability(row + 1, column + 1):
                        if self.validate_place(row + 1, column + 1):
                            self._board.place_piece(row + 1, column + 1, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row + 1][column + 1] == first_piece and \
                        self._board.board[row + 2][column + 2] == first_piece and \
                        self._board.board[row + 3][column + 3] == first_piece:
                    if self._board.check_availability(row, column):
                        if self.validate_place(row, column):
                            self._board.place_piece(row, column, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

        # We check if the computer can block the enemy on a negative diagonal
        for column in range(self._board.number_of_columns - 3):
            for row in range(3, self._board.number_of_rows):
                if self._board.board[row][column] == first_piece and\
                        self._board.board[row - 1][column + 1] == first_piece \
                        and self._board.board[row - 2][column + 2] == first_piece:
                    if self._board.check_availability(row - 3, column + 3):
                        if self.validate_place(row - 3, column + 3):
                            self._board.place_piece(row - 3, column + 3, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == first_piece and\
                        self._board.board[row - 1][column + 1] == first_piece and \
                        self._board.board[row - 3][column + 3] == first_piece:
                    if self._board.check_availability(row - 2, column + 2):
                        if self.validate_place(row - 2, column + 2):
                            self._board.place_piece(row - 2, column + 2, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == first_piece and \
                        self._board.board[row - 2][column + 2] == first_piece and \
                        self._board.board[row - 3][column + 3] == first_piece:
                    if self._board.check_availability(row - 1, column + 1):
                        if self.validate_place(row - 1, column + 1):
                            self._board.place_piece(row - 1, column + 1, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row - 1][column + 1] == first_piece and \
                        self._board.board[row - 2][column + 2] == first_piece and \
                        self._board.board[row - 3][column + 3] == first_piece:
                    if self._board.check_availability(row, column):
                        if self.validate_place(row, column):
                            self._board.place_piece(row, column, second_piece)
                            a_move_was_made = True
                            return a_move_was_made

        if not a_move_was_made:
            return False

    def win_computer(self, piece):
        """
        With this function we check if the computer can make a winning move, and if it can then it places the piece
        there
        :param piece: computer's piece
        :return: it returns true if the computer can win and false if not
        """
        a_move_was_made = False

        # We check if the computer can make a winning move on a row
        for column in range(self._board.number_of_columns - 3):
            for row in range(self._board.number_of_rows):
                if self._board.board[row][column] == piece and \
                        self._board.board[row][column + 1] == piece and \
                        self._board.board[row][column + 2] == piece:
                    if self._board.check_availability(row, column + 3):
                        if self.validate_place(row, column + 3):
                            self._board.place_piece(row, column + 3, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == piece and \
                        self._board.board[row][column + 1] == piece and \
                        self._board.board[row][column + 3] == piece:
                    if self._board.check_availability(row, column + 2):
                        if self.validate_place(row, column + 2):
                            self._board.place_piece(row, column + 2, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == piece and \
                        self._board.board[row][column + 2] == piece and \
                        self._board.board[row][column + 3] == piece:
                    if self._board.check_availability(row, column + 1):
                        if self.validate_place(row, column + 1):
                            self._board.place_piece(row, column + 1, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column + 1] == piece and \
                        self._board.board[row][column + 2] == piece and \
                        self._board.board[row][column + 3] == piece:
                    if self._board.check_availability(row, column):
                        if self.validate_place(row, column):
                            self._board.place_piece(row, column, piece)
                            a_move_was_made = True
                            return a_move_was_made

        # We check if the computer can make a winning move on a column
        for column in range(self._board.number_of_columns):
            for row in range(self._board.number_of_rows - 3):
                if self._board.board[row][column] == piece and \
                        self._board.board[row + 1][column] == piece and \
                        self._board.board[row + 2][column] == piece:
                    if self._board.check_availability(row + 3, column):
                        self._board.place_piece(row + 3, column, piece)
                        a_move_was_made = True
                        return a_move_was_made

        # We check if the computer can make a winning move on a positive diagonal
        for column in range(self._board.number_of_columns - 3):
            for row in range(self._board.number_of_rows - 3):
                if self._board.board[row][column] == piece and\
                        self._board.board[row + 1][column + 1] == piece and \
                        self._board.board[row + 2][column + 2] == piece:
                    if self._board.check_availability(row + 3, column + 3):
                        if self.validate_place(row + 3, column + 3):
                            self._board.place_piece(row + 3, column + 3, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == piece and\
                        self._board.board[row + 1][column + 1] == piece and \
                        self._board.board[row + 3][column + 3] == piece:
                    if self._board.check_availability(row + 2, column + 2):
                        if self.validate_place(row + 2, column + 2):
                            self._board.place_piece(row + 2, column + 2, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == piece and \
                        self._board.board[row + 2][column + 2] == piece and \
                        self._board.board[row + 3][column + 3] == piece:
                    if self._board.check_availability(row + 1, column + 1):
                        if self.validate_place(row + 1, column + 1):
                            self._board.place_piece(row + 1, column + 1, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row + 1][column + 1] == piece and \
                        self._board.board[row + 2][column + 2] == piece and \
                        self._board.board[row + 3][column + 3] == piece:
                    if self._board.check_availability(row, column):
                        if self.validate_place(row, column):
                            self._board.place_piece(row, column, piece)
                            a_move_was_made = True
                            return a_move_was_made

        # We check if the computer can make a winning move on a negative diagonal
        for column in range(self._board.number_of_columns - 3):
            for row in range(3, self._board.number_of_rows):
                if self._board.board[row][column] == piece and self._board.board[row - 1][column + 1] == piece and \
                        self._board.board[row - 2][column + 2] == piece:
                    if self._board.check_availability(row - 3, column + 3):
                        if self.validate_place(row - 3, column + 3):
                            self._board.place_piece(row - 3, column + 3, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == piece and self._board.board[row - 1][column + 1] == piece and \
                        self._board.board[row - 3][column + 3] == piece:
                    if self._board.check_availability(row - 2, column + 2):
                        if self.validate_place(row - 2, column + 2):
                            self._board.place_piece(row - 2, column + 2, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row][column] == piece and self._board.board[row - 2][column + 2] == piece and \
                        self._board.board[row - 3][column + 3] == piece:
                    if self._board.check_availability(row - 1, column + 1):
                        if self.validate_place(row - 1, column + 1):
                            self._board.place_piece(row - 1, column + 1, piece)
                            a_move_was_made = True
                            return a_move_was_made

                elif self._board.board[row - 1][column + 1] == piece \
                    and self._board.board[row - 2][column + 2] == piece\
                        and self._board.board[row - 3][column + 3] == piece:
                    if self._board.check_availability(row, column):
                        if self.validate_place(row, column):
                            self._board.place_piece(row, column, piece)
                            a_move_was_made = True
                            return a_move_was_made

        if not a_move_was_made:
            return False

    def random_move(self, piece):
        """
        With this function the computer places its piece randomly on a valid place
        :param piece: computer's piece
        :return: it doesn't return anything
        """
        done = False
        while not done:
            column = random.randint(0, self._board.number_of_columns-1)
            row = random.randint(0, self._board.number_of_rows-1)
            if not done and self._board.check_availability(row, column) and self.validate_place(row, column):
                self._board.place_piece(row, column, piece)
                done = True

    def winning_move(self, piece):
        """
        With this function we check if the human player made a winning move
        :param piece: human's piece
        :return: it returns true if the human wins and false if not
        """
        #  Check all the horizontal locations for win
        for column in range(self._board.number_of_columns - 3):
            for row in range(self._board.number_of_rows):
                if self._board.board[row][column] == piece and self._board.board[row][column + 1] == piece and \
                        self._board.board[row][column + 2] == piece and self._board.board[row][column + 3] == piece:
                    return True

        #  Check all the vertical locations for win
        for column in range(self._board.number_of_columns):
            for row in range(self._board.number_of_rows - 3):
                if self._board.board[row][column] == piece and self._board.board[row + 1][column] == piece and \
                        self._board.board[row + 2][column] == piece and self._board.board[row + 3][column] == piece:
                    return True

        #  Check all the positively sloped diagonals
        for column in range(self._board.number_of_columns - 3):
            for row in range(self._board.number_of_rows - 3):
                if self._board.board[row][column] == piece and self._board.board[row + 1][column + 1] == piece and \
                        self._board.board[row + 2][column + 2] == piece and\
                        self._board.board[row + 3][column + 3] == piece:
                    return True

        #  Check all the negatively sloped diagonals
        for column in range(self._board.number_of_columns - 3):
            for row in range(3, self._board.number_of_rows):
                if self._board.board[row][column] == piece and self._board.board[row - 1][column + 1] == piece and \
                        self._board.board[row - 2][column + 2] == piece and\
                        self._board.board[row - 3][column + 3] == piece:
                    return True

    def check_if_draw(self):
        """
        With this function we check if the board is full and there are no four connected pieces
        :return: it returns true if it is a draw and false if not
        """
        counter = 0
        for column in range(self._board.number_of_columns):
            for row in range(self._board.number_of_rows):
                if self._board.board[row][column] != 0:
                    counter = counter + 1
        if counter == self._board.number_of_columns*self._board.number_of_rows:
            return True
        else:
            return False


