import sys
import pygame
import math
from src.Validation.validation import Validation


class GUI:

    def __init__(self, board, service):
        self._board = board
        self._service = service
        self._square_size = 100
        self._rectangle_color = (128, 0, 128)
        self._black = (0, 0, 0)
        self._first_piece = (255, 105, 180)
        self._second_piece = (153, 50, 204)
        self._radius = self._square_size / 2 - 5
        self._width = self._board.number_of_columns * self._square_size
        self._height = (self._board.number_of_rows + 1) * self._square_size
        self._size = (self._width, self._height)
        self._screen = pygame.display.set_mode(self._size)
        pygame.font.init()
        pygame.mixer.init()
        self._font = pygame.font.SysFont("monospace", 55)
        self._print_font = pygame.font.SysFont("monospace", 22, bold=True)

    def draw_board(self):
        """
        With this function we draw the graphical board
        :return: it doesn't return anything
        """
        for column in range(self._board.number_of_columns):
            for row in range(self._board.number_of_rows):
                pygame.draw.rect(self._screen, self._rectangle_color,
                                 (column * self._square_size, row * self._square_size + self._square_size,
                                  self._square_size, self._square_size))
                pygame.draw.circle(self._screen, self._black,
                                   (column * self._square_size + self._square_size / 2,
                                    row * self._square_size + self._square_size + self._square_size / 2),
                                   self._radius)
        for column in range(self._board.number_of_columns):
            for row in range(self._board.number_of_rows):
                if self._board.board[row][column] == 0:
                    pygame.draw.circle(self._screen, self._black,
                                       (int(column * self._square_size + self._square_size / 2),
                                        self._height - int(row * self._square_size + self._square_size / 2)),
                                       self._radius)
                if self._board.board[row][column] == 1:
                    pygame.draw.circle(self._screen, self._first_piece,
                                       (int(column * self._square_size + self._square_size / 2), self._height -
                                        int(row * self._square_size + self._square_size / 2)), self._radius)
                elif self._board.board[row][column] == 2:
                    pygame.draw.circle(self._screen, self._second_piece,
                                       (int(column * self._square_size + self._square_size / 2),
                                        self._height - int(row * self._square_size + self._square_size / 2)),
                                       self._radius)
        pygame.display.update()

    def validate_start_input(self, user_text):
        okay = Validation.validate_user_choice(user_text)
        if not okay:
            self._screen.fill(self._black)
            label1 = self._print_font.render("Invalid input!!! Try again!!!", True, self._first_piece)
            self._screen.blit(label1, (0, 0))
            pygame.display.flip()
            pygame.time.wait(1000)
            self.start_of_the_game()
        else:
            self.choose_type_of_game(user_text)

    def validate_second_input(self, user_text):
        okay = Validation.validate_user_choice(user_text)
        if not okay:
            self._screen.fill(self._black)
            label1 = self._print_font.render("Invalid input!!! Try again!!!", True, self._first_piece)
            self._screen.blit(label1, (0, 0))
            pygame.display.flip()
            pygame.time.wait(1000)
            self.choose_your_side()
        else:
            self.finalize_choosing_the_side(user_text)

    def start_of_the_game(self):
        #pygame.mixer.music.load("C:/Users/Alexandra/Desktop/Facultate/connect_four.mp3")
        #pygame.mixer.music.play(-1)
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        self._screen.fill(self._black)
        label = self._print_font.render("Type 1 for human vs human, or 2 for human vs computer", True,
                                        self._second_piece)
        self._screen.blit(label, (0, 0))
        user_text = ''
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    user_text = user_text + event.unicode
                    text_surface = self._print_font.render(user_text, True, self._first_piece)
                    self._screen.blit(text_surface, (0, 30))
                    pygame.display.flip()
                    if event.key == pygame.K_RETURN:
                        done = True
                        self.validate_start_input(user_text)

    def choose_type_of_game(self, user_text):
        if user_text == '1':
            self.human_vs_human()
        elif user_text == '2':
            self.choose_your_side()

    def choose_your_side(self):
        self._screen.fill(self._black)
        label = self._print_font.render("For starting first type 1, else type 2!", True, self._second_piece)
        self._screen.blit(label, (0, 0))
        user_text = ''
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    user_text = user_text + event.unicode
                    text_surface = self._print_font.render(user_text, True, self._first_piece)
                    self._screen.blit(text_surface, (0, 30))
                    pygame.display.flip()
                    if event.key == pygame.K_RETURN:
                        done = True
                        self.validate_second_input(user_text)
                        self.finalize_choosing_the_side(user_text)

    def finalize_choosing_the_side(self, user_text):
        if user_text == '1':
            human_turn = 1
            human_piece = 1
            computer_turn = 2
            computer_piece = 2
            self.human_vs_computer(human_turn, human_piece, computer_turn, computer_piece)

        elif user_text == '2':
            human_turn = 2
            human_piece = 1
            computer_turn = 1
            computer_piece = 2
            self.human_vs_computer(human_turn, human_piece, computer_turn, computer_piece)

    def human_vs_human(self):
        self.draw_board()
        turn = 0
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self._screen, self._black, (0, 0, self._width, self._square_size))
                    position_of_x = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(self._screen, self._first_piece, (position_of_x, int(self._square_size / 2)),
                                           self._radius)
                    else:
                        pygame.draw.circle(self._screen, self._second_piece,
                                           (position_of_x, int(self._square_size / 2)),
                                           self._radius)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == 0:
                        pygame.draw.rect(self._screen, self._black, (0, 0, self._width, self._square_size))
                        position_of_x = event.pos[0]
                        selected_column = int(math.floor(position_of_x / self._square_size))

                        if self._board.is_free(selected_column):
                            row = self._board.get_new_open_row(selected_column)
                            self._board.place_piece(row, selected_column, 1)

                            if self._service.winning_move(1):
                                label = self._font.render("Player 1 wins!!!", True, self._first_piece)
                                self._screen.blit(label, (40, 10))
                                game_over = True

                        if self._service.check_if_draw():
                            label = self._font.render("It is a draw!", True, self._first_piece)
                            self._screen.blit(label, (40, 10))
                            game_over = True

                    else:
                        pygame.draw.rect(self._screen, self._black, (0, 0, self._width, self._square_size))
                        position_of_x = event.pos[0]
                        selected_column = int(math.floor(position_of_x / self._square_size))

                        if self._board.is_free(selected_column):
                            row = self._board.get_new_open_row(selected_column)
                            self._board.place_piece(row, selected_column, 2)

                            if self._service.winning_move(2):
                                label = self._font.render("Player 2 wins!!!", True, self._second_piece)
                                self._screen.blit(label, (40, 10))
                                game_over = True

                        if self._service.check_if_draw():
                            label = self._font.render("It is a draw!", True, self._first_piece)
                            self._screen.blit(label, (40, 10))
                            game_over = True

                    self.draw_board()
                    turn = turn + 1
                    turn = turn % 2
        if game_over:
            pygame.time.wait(3000)
            sys.exit()

    def human_vs_computer(self, human_turn, human_piece, computer_turn, computer_piece):
        self.draw_board()
        turn = 1
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self._screen, self._black, (0, 0, self._width, self._square_size))
                    position_of_x = event.pos[0]
                    if turn == human_turn:
                        pygame.draw.circle(self._screen, self._first_piece, (position_of_x, int(self._square_size / 2)),
                                           self._radius)
                    else:
                        pygame.draw.circle(self._screen, self._second_piece,
                                           (position_of_x, int(self._square_size / 2)),
                                           self._radius)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == human_turn:
                        pygame.draw.rect(self._screen, self._black, (0, 0, self._width, self._square_size))
                        position_of_x = event.pos[0]
                        selected_column = int(math.floor(position_of_x / self._square_size))

                        if self._board.is_free(selected_column):
                            row = self._board.get_new_open_row(selected_column)
                            self._board.place_piece(row, selected_column, 1)
                            turn = computer_turn

                            if self._service.winning_move(1):
                                label = self._font.render("Player 1 wins!!!", True, self._first_piece)
                                self._screen.blit(label, (40, 10))
                                game_over = True

                        if self._service.check_if_draw():
                            label = self._font.render("It is a draw!", True, self._first_piece)
                            self._screen.blit(label, (40, 10))
                            game_over = True

                        self.draw_board()

            if turn == computer_turn:
                if self._service.win_computer(computer_piece):
                    label = self._font.render("Computer wins!!!", True, self._second_piece)
                    self._screen.blit(label, (40, 10))
                    game_over = True

                elif self._service.block_enemy(human_piece, computer_piece):
                    turn = human_turn
                else:
                    self._service.random_move(computer_piece)
                    turn = human_turn

                if self._service.check_if_draw():
                    label = self._font.render("It is a draw!", True, self._first_piece)
                    self._screen.blit(label, (40, 10))
                    game_over = True

                self.draw_board()

        if game_over:
            pygame.time.wait(3000)
            sys.exit()


