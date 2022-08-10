import unittest
from src.Validation.validation import Validation
from src.Domain.board import Board, GameException
from src.Service.service import Service


class Test(unittest.TestCase):

    def test_validate_ship_input(self):
        validation = Validation()
        pos = 'A1A2A3'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = '1ABCDC'
        self.assertEqual(validation.validate_ship_input(pos), False)

        pos = 'A11Bc2'
        self.assertEqual(validation.validate_ship_input(pos), False)

        pos = 'A1B122'
        self.assertEqual(validation.validate_ship_input(pos), False)

        pos = 'ABB1C2'
        self.assertEqual(validation.validate_ship_input(pos), False)

        pos = 'ABB1C'
        self.assertEqual(validation.validate_ship_input(pos), False)

        pos = 'A1BDC2'
        self.assertEqual(validation.validate_ship_input(pos), False)

        pos = 'A1B1CD'
        self.assertEqual(validation.validate_ship_input(pos), False)

        pos = 'B2B3B4'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = 'B3B4B5'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = 'B0B1B2'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = 'A1B1C1'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = 'B1C1D1'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = 'C1D1E1'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = 'D1E1F1'
        self.assertEqual(validation.validate_ship_input(pos), True)

        pos = 'C1E1F1'
        self.assertEqual(validation.validate_ship_input(pos), False)

    def test_check_if_free(self):
        board = Board()
        service = Service(board)
        board.player_board[1][1] = 1
        self.assertEqual(service.check_if_free(1, 1), False)
        self.assertEqual(service.check_if_free(2, 2), True)

    def test_check_number_of_ships(self):
        board = Board()
        service = Service(board)
        service.ships.append(0)
        service.ships.append(0)
        service.ships[0] = 'A1B1C1'
        service.ships[1] = 'B2B3B4'
        service.check_number_of_ships()
        self.assertEqual(service.ships[0], 'B2B3B4')

    def test_clear_ship_from_board(self):
        board = Board()
        service = Service(board)
        service.ships.append(0)
        service.ships.append(0)
        service.ships[0] = 'B2B3B4'
        service.ships[1] = 'A1B1C1'
        service.clear_ship_from_board()
        self.assertEqual(board.player_board[2][2], 0)
        self.assertEqual(board.player_board[3][2], 0)
        self.assertEqual(board.player_board[4][2], 0)

    def test_place_players_piece(self):
        board = Board()
        service = Service(board)
        command = 'B2B3B4'
        service.place_players_piece(command)
        self.assertEqual(board.player_board[2][2], 1)
        self.assertEqual(board.player_board[3][2], 1)
        self.assertEqual(board.player_board[4][2], 1)
        command = 'B2C2D2'
        with self.assertRaises(GameException):
            service.place_players_piece(command)

        command = 'C3D3E3'
        service.place_players_piece(command)
        self.assertEqual(board.player_board[3][3], 1)
        self.assertEqual(board.player_board[3][4], 1)
        self.assertEqual(board.player_board[3][5], 1)

        command = 'C3C4C5'
        with self.assertRaises(GameException):
            service.place_players_piece(command)
