from src.Domain.board import Board
from src.Service.service import Service
from src.Ui.console import Console
from src.Validation.validation import Validation

validation = Validation()
board = Board()
service = Service(board)
start = Console(service, board, validation)

start.start()