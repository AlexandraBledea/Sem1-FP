from src.Service.random_strategy import RandomStrategy
from src.Domain.Board import Board
import unittest
import numpy as np


class TestRandomStrategy(unittest.TestCase):

    def test_validate_place(self):
        board = Board()
        service = RandomStrategy(board)

        self.assertEqual(service.validate_place(4, 0), False)
        self.assertEqual(service.validate_place(0, 0), True)
        board.board[0][0] = 1
        board.board[1][0] = 1
        self.assertEqual(service.validate_place(2, 0), True)
        board.board[2][0] = 1
        self.assertEqual(service.validate_place(3, 0), True)
        board.board[3][0] = 1
        self.assertEqual(service.validate_place(4, 0), True)
        board.board[4][0] = 1
        self.assertEqual(service.validate_place(5, 0), True)
        board.board[5][0] = 1
        self.assertEqual(service.validate_place(6, 0), True)


    def test_block_enemy(self):

        board = Board()
        service = RandomStrategy(board)

        #  Test block enemy on row

        board.board[0][0] = 1
        board.board[0][1] = 1
        board.board[0][2] = 1
        self.assertEqual(service.block_enemy(1, 2), True)
        board.board[0][0] = 1
        board.board[0][1] = 1
        board.board[0][2] = 0
        board.board[0][3] = 1
        self.assertEqual(service.block_enemy(1, 2), True)
        board.board[0][0] = 1
        board.board[0][1] = 0
        board.board[0][2] = 1
        board.board[0][3] = 1
        self.assertEqual(service.block_enemy(1, 2), True)
        board.board[0][0] = 0
        board.board[0][1] = 1
        board.board[0][2] = 1
        board.board[0][3] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0

        # Test block enemy on column

        board.board[0][0] = 1
        board.board[1][0] = 1
        board.board[2][0] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[1][0] = 0
        board.board[2][0] = 0
        board.board[3][0] = 0

        # Test block enemy on positive diagonal

        board.board[0][0] = 1
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 1
        board.board[2][3] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        board.board[0][0] = 1
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 0
        board.board[2][3] = 1
        board.board[3][3] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        board.board[0][0] = 1
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 0
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 1
        board.board[2][3] = 1
        board.board[3][3] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        board.board[0][0] = 0
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 1
        board.board[2][3] = 1
        board.board[3][3] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0
        board.board[1][1] = 0
        board.board[1][2] = 0
        board.board[1][3] = 0
        board.board[2][2] = 0
        board.board[2][3] = 0
        board.board[3][3] = 0

        # Test block enemy on negative diagonal

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[2][0] = 1
        board.board[2][1] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[2][0] = 1
        board.board[2][1] = 0
        board.board[3][0] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 0
        board.board[2][0] = 1
        board.board[2][1] = 1
        board.board[3][0] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 0
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[2][0] = 1
        board.board[2][1] = 1
        board.board[3][0] = 1
        self.assertEqual(service.block_enemy(1, 2), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0
        board.board[1][0] = 0
        board.board[1][1] = 0
        board.board[1][2] = 0
        board.board[2][0] = 0
        board.board[2][1] = 0
        board.board[3][0] = 0

        self.assertEqual(service.block_enemy(1, 2), False)

    def test_win_computer(self):
        board = Board()
        service = RandomStrategy(board)

        #  Test win computer on row

        board.board[0][0] = 1
        board.board[0][1] = 1
        board.board[0][2] = 1
        self.assertEqual(service.win_computer(1), True)
        board.board[0][0] = 1
        board.board[0][1] = 1
        board.board[0][2] = 0
        board.board[0][3] = 1
        self.assertEqual(service.win_computer(1), True)
        board.board[0][0] = 1
        board.board[0][1] = 0
        board.board[0][2] = 1
        board.board[0][3] = 1
        self.assertEqual(service.win_computer(1), True)
        board.board[0][0] = 0
        board.board[0][1] = 1
        board.board[0][2] = 1
        board.board[0][3] = 1
        self.assertEqual(service.win_computer(1), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0

        # Test win computer on column

        board.board[0][0] = 1
        board.board[1][0] = 1
        board.board[2][0] = 1
        self.assertEqual(service.win_computer(1), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[1][0] = 0
        board.board[2][0] = 0
        board.board[3][0] = 0

        # Test win computer on positive diagonal

        board.board[0][0] = 1
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 1
        board.board[2][3] = 1
        self.assertEqual(service.win_computer(1), True)

        board.board[0][0] = 1
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 0
        board.board[2][3] = 1
        board.board[3][3] = 1
        self.assertEqual(service.win_computer(1), True)

        board.board[0][0] = 1
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 0
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 1
        board.board[2][3] = 1
        board.board[3][3] = 1
        self.assertEqual(service.win_computer(1), True)

        board.board[0][0] = 0
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 1
        board.board[2][3] = 1
        board.board[3][3] = 1
        self.assertEqual(service.win_computer(1), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0
        board.board[1][1] = 0
        board.board[1][2] = 0
        board.board[1][3] = 0
        board.board[2][2] = 0
        board.board[2][3] = 0
        board.board[3][3] = 0

        # Test win computer on negative diagonal

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[2][0] = 1
        board.board[2][1] = 1
        self.assertEqual(service.win_computer(1), True)

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[2][0] = 1
        board.board[2][1] = 0
        board.board[3][0] = 1
        self.assertEqual(service.win_computer(1), True)

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 0
        board.board[2][0] = 1
        board.board[2][1] = 1
        board.board[3][0] = 1
        self.assertEqual(service.win_computer(1), True)

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 0
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[2][0] = 1
        board.board[2][1] = 1
        board.board[3][0] = 1
        self.assertEqual(service.win_computer(1), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0
        board.board[1][0] = 0
        board.board[1][1] = 0
        board.board[1][2] = 0
        board.board[2][0] = 0
        board.board[2][1] = 0
        board.board[3][0] = 0

        self.assertEqual(service.win_computer(1), False)

    def test_winning_move(self):

        board = Board()
        service = RandomStrategy(board)

        # Test winning move on row

        board.board[0][0] = 1
        board.board[0][1] = 1
        board.board[0][2] = 1
        board.board[0][3] = 1

        self.assertEqual(service.winning_move(1), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0

        # Test winning move on column

        board.board[0][0] = 1
        board.board[1][0] = 1
        board.board[2][0] = 1
        board.board[3][0] = 1

        self.assertEqual(service.winning_move(1), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[1][0] = 0
        board.board[2][0] = 0
        board.board[3][0] = 0

        # Test winning move on positive diagonal

        board.board[0][0] = 1
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[2][2] = 1
        board.board[2][3] = 1
        board.board[3][3] = 1
        self.assertEqual(service.winning_move(1), True)

        # Reinitialize the matrix

        board.board[0][0] = 0
        board.board[0][1] = 0
        board.board[0][2] = 0
        board.board[0][3] = 0
        board.board[1][1] = 0
        board.board[1][2] = 0
        board.board[1][3] = 0
        board.board[2][2] = 0
        board.board[2][3] = 0
        board.board[3][3] = 0

        # Test winning move on negative diagonal

        board.board[0][0] = 2
        board.board[0][1] = 2
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[1][0] = 2
        board.board[1][1] = 1
        board.board[1][2] = 1
        board.board[2][0] = 1
        board.board[2][1] = 1
        board.board[3][0] = 1
        self.assertEqual(service.winning_move(1), True)

    def test_check_if_draw(self):

        board = Board()
        service = RandomStrategy(board)

        self.assertEqual(service.check_if_draw(), False)

        board.board[0][0] = 2
        board.board[0][1] = 1
        board.board[0][2] = 2
        board.board[0][3] = 1
        board.board[0][4] = 2
        board.board[0][5] = 1
        board.board[0][6] = 2
        board.board[1][0] = 1
        board.board[1][1] = 2
        board.board[1][2] = 1
        board.board[1][3] = 2
        board.board[1][4] = 1
        board.board[1][5] = 2
        board.board[1][6] = 1
        board.board[2][0] = 2
        board.board[2][1] = 1
        board.board[2][2] = 2
        board.board[2][3] = 1
        board.board[2][4] = 2
        board.board[2][5] = 1
        board.board[2][6] = 2
        board.board[3][0] = 2
        board.board[3][1] = 1
        board.board[3][2] = 2
        board.board[3][3] = 1
        board.board[3][4] = 2
        board.board[3][5] = 1
        board.board[3][6] = 2
        board.board[4][0] = 1
        board.board[4][1] = 1
        board.board[4][2] = 2
        board.board[4][3] = 1
        board.board[4][4] = 2
        board.board[4][5] = 1
        board.board[4][6] = 2
        board.board[5][0] = 2
        board.board[5][1] = 2
        board.board[5][2] = 1
        board.board[5][3] = 2
        board.board[5][4] = 1
        board.board[5][5] = 2
        board.board[5][6] = 1
        self.assertEqual(service.check_if_draw(), True)

    def test_random_move(self):

        board = Board()
        service = RandomStrategy(board)

        service.random_move(1)
        for column in range(board.number_of_columns):
            for row in range(board.number_of_rows):
                if board.board[row][column] == 1:
                    okay = True

        self.assertEqual(okay, True)
        

