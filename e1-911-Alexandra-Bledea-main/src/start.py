from src.Domain.board import Board
from src.Service.service import Game
from src.Console.console import Console


file = open("input.txt", 'r+')
input_ = file.read().split()
dimension = int(input_[0])
apples = int(input_[1])
board = Board(dimension, apples)
service = Game(board)
console = Console(service, board)
console.start()
