import texttable

from src.Domain.board import GameException


class Console:

    def __init__(self, service, board, validate):
        self.service = service
        self.board = board
        self.validate = validate

    def display_board(self):
        print(str(self.board))

    def cheat(self, command):
        t = texttable.Texttable()
        header = [' ']

        for h in range(6):
            header.append(chr(65 + h))

        t.header(header)

        for row in range(0, 6):
            data = []

            for val in self.board.enemy_board[row][1:-1]:
                if val == 0:
                    data.append(".")
                elif val == 1:
                    data.append("+")
                elif val == 2:
                    data.append('X')
                elif val == 3:
                    data.append('o')

            t.add_row([row] + data)
        print(t.draw())

    def place_ship(self, command):
        """
        With this function we place the players ship on its board
        :param command: the position for the ship
        :return: it doesn't return anything
        """
        if not self.validate.validate_ship_input(command):
            raise GameException("Invalid input!")

        self.service.place_players_piece(command)
        self.display_board()

    def attack_player(self, params):
        if not self.validate.validate_input_attack(params):
            raise GameException("Invalid input!")
        if self.service.check_players_attack_position(params):
            self.display_board()
            return True

    def start_of_game(self, command):
        self.service.clear_enemy_board()
        self.service.place_computers_ships()
        commands_2_dict = {'cheat': self.cheat, 'attack': self.attack_player}
        turn = 1
        game_over = False
        while not game_over:
            if turn == 1:
                okay = False
                while not okay:
                    command = input("Command>")
                    command_word, command_params = self.service.split_command(command)
                    if command_word in commands_2_dict:
                        try:
                            okay = commands_2_dict[command_word](command_params)

                        except ValueError as ve:
                            print(ve)

                        except GameException as ge:
                            print(ge)
                    else:
                        print("Invalid command!")
                if self.service.check_player_wins() == 6:
                    print("Human player wins!!!")
                    game_over = True
                turn = 0
            elif turn == 0:
                self.service.enemy_attack_position()
                self.display_board()
                if self.service.check_enemy_wins() == 6:
                    print("Computer wins!!!")
                    game_over = True
                turn = 1

    def start(self):

        command_dict = {'ship': self.place_ship, 'cheat': self.cheat, 'start': self.start_of_game}

        done = False

        while not done:
            command = input("Command> ")
            command_word, command_params = self.service.split_command(command)
            if command_word in command_dict:
                try:
                    command_dict[command_word](command_params)

                except ValueError as ve:
                    print(ve)

                except GameException as ge:
                    print(ge)
            elif 'exit' == command_word:
                done = True
            else:
                print("Invalid command!")