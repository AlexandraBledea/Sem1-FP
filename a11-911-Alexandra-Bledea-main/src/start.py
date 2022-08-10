from src.Domain.Board import Board
from src.Service.random_strategy import RandomStrategy
from src.UI.UI import UI
from src.GUI.GUI import GUI

board = Board()
service = RandomStrategy(board)
gui = GUI(board, service)
gui.start_of_the_game()
#ui = UI(board, service)
#ui.start_of_the_game()
