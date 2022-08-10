from src.Domain.Board import Board, GameException
import unittest


class TestBoard(unittest.TestCase):

    def test_check_availability(self):
        board = Board()
        board.board[1][2] = 2
        board.board[5][6] = 1
        self.assertEqual(board.check_availability(0, 0), True)
        self.assertEqual(board.check_availability(1, 2), False)
        self.assertEqual(board.check_availability(board.number_of_rows - 1, board.number_of_columns - 1), False)

    def test_is_free(self):
        board = Board()
        board.board[5][6] = 2
        self.assertEqual(board.is_free(6), False)
        self.assertEqual(board.is_free(5), True)

    def test_get_new_open_row(self):
        board = Board()
        board.board[0][0] = 1
        self.assertEqual(board.get_new_open_row(0), 1)
        self.assertEqual(board.get_new_open_row(1), 0)

    def test_place_piece(self):
        board = Board()
        board.place_piece(0, 0, 1)
        self.assertEqual(board.board[0][0], 1)
        self.assertNotEqual(board.board[0][0], 0)

    def test_game_exception(self):
        exception = GameException("Invalid data!")
        self.assertEqual(str(exception), "Invalid data!")
