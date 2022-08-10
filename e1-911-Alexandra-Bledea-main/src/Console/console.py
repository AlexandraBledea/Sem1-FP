from src.Domain.board import GameException


class Console:

    def __init__(self, service, board):
        self.service = service
        self.board = board

    def draw_board(self):
        print(str(self.board))

    def move_snake(self, params, done):
        if params == '':
            params = 1
        else:
            params = int(params)
        if self.service.move_snake_with_move_command(params):
            print("Game over!")
            done = True
            return done

    def move_snake_right(self, params, done):
        if self.service.move_snake_to_right():
            print("Game over!")
            done = True
            return done

    def move_snake_left(self, params, done):
        if self.service.move_snake_to_left_2():
            print("Game over!")
            done = True
            return done

    def start(self):

        command_dict = {'move': self.move_snake, 'left': self.move_snake_left, 'right': self.move_snake_right}

        done = False
        self.draw_board()
        while not done:
            command = input("Command> ")
            command_word, command_params = self.service.split_command(command)
            if command_word in command_dict:
                try:
                    done = command_dict[command_word](command_params, done)
                    self.draw_board()
                except ValueError as ve:
                    print(ve)

                except GameException as ge:
                    print(ge)
            elif 'exit' == command_word:
                done = True
            else:
                print("Invalid command!")