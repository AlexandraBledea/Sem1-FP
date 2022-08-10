from src.Domain.player import Player
from src.Repository.repo import Repository
from src.Repository.repotextfile import RepoTextFile
from src.Service.service import Service
from src.Console.console import Console

repository = Repository()
service = Service()
console = Console(service, repository)

console.start_command_ui()
