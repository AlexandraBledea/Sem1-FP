from src.Domain.board import GameException
from src.Validation.validation import Validation
import random


class Service:

    def __init__(self, board):
        self._board = board
        self.ships = []

    def clear_enemy_board(self):
        for i in range(0, self._board.rows):
            for j in range(1, self._board.columns + 1):
                self._board.enemy_board[i][j] = 0

    def check_players_attack_position(self, params):
        column = ord(params[0]) - ord('A') + 1
        row = ord(params[1]) - ord('0')
        if self._board.enemy_board[row][column] == 3 or self._board.enemy_board[row][column] == 2:
            raise GameException("The chosen position for attack is invalid!")
        elif self._board.enemy_board[row][column] == 1:
            self._board.place_piece_enemy(row, column, 2)
        else:
            self._board.place_piece_enemy(row, column, 3)
        return True

    def check_enemy_wins(self):
        count = 0
        for i in range(0, self._board.rows):
            for j in range(1, self._board.columns + 1):
                if self._board.player_board[i][j] == 2:
                    count = count + 1
        return count
 
    def check_player_wins(self):
        count = 0
        for i in range(0, self._board.rows):
            for j in range(1, self._board.columns + 1):
                if self._board.enemy_board[i][j] == 2:
                    count = count + 1
        return count

    def enemy_attack_position(self):
        validate = Validation()
        done = False
        while not done:
            count = 0
            while count < 1:
                command = []
                letters = ['A', 'B', 'C', 'D', 'E', 'F']
                row = random.randint(0, 6)
                column = random.choice(letters)
                command.append(column)
                command.append(str(row))
                if validate.validate_input_attack(command):
                    count = count + 1
            if self.check_enemy_attack_position(command):
                done = True

    def check_enemy_attack_position(self, command):
        column = ord(command[0]) - ord('A') + 1
        row = int(command[1])
        if self._board.player_board[row][column] == 3 or self._board.player_board[row][column] == 2:
            return False
        elif self._board.player_board[row][column] == 1:
            self._board.place_piece_player(row, column, 2)
            return True
        else:
            self._board.place_piece_player(row, column, 3)
            return True

    def place_computers_ships(self):
        validate = Validation()
        commands = []
        count_ships = 0
        while count_ships < 1:
            command = []
            letters = ['A', 'B', 'C', 'D', 'E', 'F']
            for i in range(0, 3):
                row = random.randint(0, 6)
                column = random.choice(letters)
                command.append(column)
                command.append(str(row))
            if validate.validate_ship_input(command):
                count_ships = count_ships + 1
                commands.append(command)

        self.place_first_ship_enemy(commands)
        self.place_second_ship_enemy()

    def place_first_ship_enemy(self, commands):
        command = commands[0]

        if command[0] == command[2] == command[4]:
            column = ord(command[0]) - ord('A') + 1
            first_row = ord(command[1]) - ord('0')
            second_row = ord(command[3]) - ord('0')
            third_row = ord(command[5]) - ord('0')

            self._board.place_piece_enemy(first_row, column, 1)
            self._board.place_piece_enemy(second_row, column, 1)
            self._board.place_piece_enemy(third_row, column, 1)

        elif command[1] == command[3] == command[5]:
            row = ord(command[1]) - ord('0')
            first_column = ord(command[0]) - ord('A') + 1
            second_column = ord(command[2]) - ord('A') + 1
            third_column = ord(command[4]) - ord('A') + 1

            self._board.place_piece_enemy(row, first_column, 1)
            self._board.place_piece_enemy(row, second_column, 1)
            self._board.place_piece_enemy(row, third_column, 1)

    def place_second_ship_enemy(self):
        validate = Validation()
        done = False
        while not done:
            commands = []
            count_ships = 0
            while count_ships < 1:
                command = []
                letters = ['A', 'B', 'C', 'D', 'E', 'F']
                for i in range(0, 3):
                    row = random.randint(0, 6)
                    column = random.choice(letters)
                    command.append(column)
                    command.append(str(row))
                if validate.validate_ship_input(command):
                    count_ships = count_ships + 1
                    commands.append(command)
            if self.check_enemy_ships(commands):
                done = True

    def check_enemy_ships(self, commands):
        command = commands[0]

        if command[0] == command[2] == command[4]:
            column = ord(command[0]) - ord('A') + 1
            first_row = ord(command[1]) - ord('0')
            second_row = ord(command[3]) - ord('0')
            third_row = ord(command[5]) - ord('0')
            if self._board.is_free_enemy(first_row, column) and self._board.is_free_enemy(second_row, column) and \
                    self._board.is_free_enemy(third_row, column):
                self._board.place_piece_enemy(first_row, column, 1)
                self._board.place_piece_enemy(second_row, column, 1)
                self._board.place_piece_enemy(third_row, column, 1)
                return True
            else:
                return False
        elif command[1] == command[3] == command[5]:
            row = ord(command[1]) - ord('0')
            first_column = ord(command[0]) - ord('A') + 1
            second_column = ord(command[2]) - ord('A') + 1
            third_column = ord(command[4]) - ord('A') + 1
            if self._board.is_free_enemy(row, first_column) and self._board.is_free_enemy(row, second_column) and \
                    self._board.is_free_enemy(row, third_column):
                self._board.place_piece_enemy(row, first_column, 1)
                self._board.place_piece_enemy(row, second_column, 1)
                self._board.place_piece_enemy(row, third_column, 1)
                return True
            else:
                return False

    def check_if_free(self, row, column):
        """
        With this function we check if that specific place on the board is free
        :param row: the row for which we check
        :param column: the column for which we check
        :return: it returns true if the place is free and false otherwise
        """
        if self._board.is_free_player(row, column):
            return True
        return False

    def check_number_of_ships(self):
        """
        With this function we check if the player already has 2 ships on the board
        If so, we delete the first one from the list and update it
        :return:
        """
        if len(self.ships) == 2:
            self.clear_ship_from_board()
            first_ship = self.ships[1]
            self.ships[0] = first_ship
            self.ships[1] = 0
            self.ships.pop()
        else:
            pass

    def clear_ship_from_board(self):
        """
        With this function we delete a ship from the players board
        :return: it doesn't return anything
        """
        command = self.ships[0]

        if command[0] == command[2] == command[4]:
            column = ord(command[0]) - ord('A') + 1
            first_row = ord(command[1]) - ord('0')
            second_row = ord(command[3]) - ord('0')
            third_row = ord(command[5]) - ord('0')

            self._board.place_piece_player(first_row, column, 0)
            self._board.place_piece_player(second_row, column, 0)
            self._board.place_piece_player(third_row, column, 0)

        elif command[1] == command[3] == command[5]:
            row = ord(command[1]) - ord('0')
            first_column = ord(command[0]) - ord('A') + 1
            second_column = ord(command[2]) - ord('A') + 1
            third_column = ord(command[4]) - ord('A') + 1

            self._board.place_piece_player(row, first_column, 0)
            self._board.place_piece_player(row, second_column, 0)
            self._board.place_piece_player(row, third_column, 0)

    def place_players_piece(self, command):
        """
        With this function we place a ship on the player's board
        :param command: The coordinates for the ship of the player
        :return: it doesn't return anything
        """
        self.check_number_of_ships()

        if command[0] == command[2] == command[4]:
            column = ord(command[0]) - ord('A') + 1
            first_row = ord(command[1]) - ord('0')
            second_row = ord(command[3]) - ord('0')
            third_row = ord(command[5]) - ord('0')
            if self.check_if_free(column, first_row) and self.check_if_free(column, second_row) and \
                    self.check_if_free(column, third_row):
                self.ships.append(command)
                self._board.place_piece_player(first_row, column, 1)
                self._board.place_piece_player(second_row, column, 1)
                self._board.place_piece_player(third_row, column, 1)

            else:
                raise GameException("Invalid place for the ship!")

        elif command[1] == command[3] == command[5]:
            row = ord(command[1]) - ord('0')
            first_column = ord(command[0]) - ord('A') + 1
            second_column = ord(command[2]) - ord('A') + 1
            third_column = ord(command[4]) - ord('A') + 1
            if self.check_if_free(row, first_column) and self.check_if_free(row, second_column) and \
                    self.check_if_free(row, third_column):

                self.ships.append(command)
                self._board.place_piece_player(row, first_column, 1)
                self._board.place_piece_player(row, second_column, 1)
                self._board.place_piece_player(row, third_column, 1)

            else:
                raise GameException("Invalid place for the ship!")

    def split_command(self, command):
        """
        With this function we split a command and some parameters
        :param command: the command we want to split
        :return: it will return the command and the parameters in two different variables
        """
        tokens = command.strip().split(' ', 1)
        tokens[0] = tokens[0].strip().lower()
        return tokens[0], '' if len(tokens) == 1 else tokens[1].strip()
