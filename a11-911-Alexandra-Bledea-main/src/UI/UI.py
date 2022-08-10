from src.Domain.Board import GameException
from src.Validation.validation import Validation


class UI:

    def __init__(self, board, service):
        self._board = board
        self._service = service

    def start_of_the_game(self):
        """
        With this function we ask the user to choose the game mode he want. Human vs human or human vs computer
        :return: it doesn't return anything
        """
        print("Choose the gameplay you want! Type 1 for human vs computer or type 2 for human vs human!")
        okay = False
        while not okay:
            type_game = input()
            okay = Validation.validate_user_choice(type_game)
            if okay:
                type_game = int(type_game)
                if type_game == 1:
                    self.human_vs_computer()
                else:
                    self.human_vs_human()
            else:
                print("Invalid input! It should be either 1 or 2! Try again!")

    def choose_your_side(self):
        """
        With this function, if the user chose to play human vs computer, we ask him to choose if now he wants to start
        first or second
        :return: it returns the human's piece, human's turn, computer's piece and computer's turn
        """
        print("Choose if you want to start first or the second!")
        print("For starting first type 1, else type 2!")
        okay = False
        while not okay:
            side = input()
            okay = Validation.validate_user_choice(side)
            if okay:
                side = int(side)
                if side == 1:
                    human_turn = 1
                    human_piece = 1
                    computer_turn = 2
                    computer_piece = 2
                elif side == 2:
                    human_turn = 2
                    human_piece = 2
                    computer_turn = 1
                    computer_piece = 1
            else:
                print("Invalid input! It should be either 1 or 2! Try again!")
        return human_turn, human_piece, computer_turn, computer_piece

    def human_vs_computer(self):
        human_turn, human_piece, computer_turn, computer_piece = self.choose_your_side()
        turn = 1
        game_over = False
        while not game_over:
            if turn == computer_turn:
                if self._service.win_computer(computer_piece):
                    print("Computer wins!!!")
                    game_over = True
                elif self._service.block_enemy(human_piece, computer_piece):
                    turn = human_turn
                else:
                    self._service.random_move(computer_piece)
                    turn = human_turn

                if self._service.check_if_draw():
                    print("It is a draw!")
                    game_over = True

            elif turn == human_turn:

                okay = False
                while not okay:
                    selection = input("Make your selection (0-6):")
                    okay = Validation.validate_input(selection)
                    if okay:
                        selection = int(selection)
                        if self._board.is_free(selection):
                            row = self._board.get_new_open_row(selection)
                            self._board.place_piece(row, selection, human_piece)
                            turn = computer_turn
                        else:
                            print("The chosen column is already full! Try again!")
                    else:
                        print("Invalid input! It should be a number between 0 and 6! Try again!")

                if self._service.winning_move(human_piece):
                    print("Human player wins!!!")
                    game_over = True

                if self._service.check_if_draw():
                    print("It is a draw!")
                    game_over = True

            self._board.print_board()
            print()
            print()

    def human_vs_human(self):

        first_human_turn = 1
        first_human_piece = 1
        second_human_turn = 2
        second_human_piece = 2
        turn = 1
        game_over = False
        while not game_over:
            if turn == first_human_turn:
                okay = False
                while not okay:
                    selection = input("Make your selection (0-6):")
                    okay = Validation.validate_input(selection)
                    if okay:
                        selection = int(selection)
                        if self._board.is_free(selection):
                            row = self._board.get_new_open_row(selection)
                            self._board.place_piece(row, selection, first_human_piece)
                            turn = second_human_turn
                        else:
                            print("The chosen column is already full! Try again!")
                    else:
                        print("Invalid input! It should be a number between 0 and 6! Try again!")

                if self._service.winning_move(first_human_piece):
                    print("First player wins!!!")
                    game_over = True

                if self._service.check_if_draw():
                    print("It is a draw!")
                    game_over = True

            else:

                okay = False

                while not okay:
                    selection = input("Make your selection (0-6):")
                    okay = Validation.validate_input(selection)
                    if okay:
                        selection = int(selection)
                        if self._board.is_free(selection):
                            row = self._board.get_new_open_row(selection)
                            self._board.place_piece(row, selection, second_human_piece)
                            turn = first_human_piece
                        else:
                            print("The chosen column is already full! Try again!")
                    else:
                        print("Invalid input! It should be a number between 0 and 6! Try again!")

                if self._service.winning_move(second_human_piece):
                    print("Second player wins!!!")
                    game_over = True

                if self._service.check_if_draw():
                    print("It is a draw!")
                    game_over = True

            self._board.print_board()
            print()
            print()
