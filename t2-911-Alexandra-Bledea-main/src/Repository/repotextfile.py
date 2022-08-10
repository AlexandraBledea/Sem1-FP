from src.Domain.player import Player
from src.Repository.repo import Repository


class RepoTextFile(Repository):

    def __init__(self, file_name):
        super(RepoTextFile, self).__init__()
        self.__file_name = file_name
        self.__load_file()

    def __load_file(self):
        try:
            file = open(self.__file_name, 'rt')
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.strip('\n')
                if line == '':
                    continue
                else:
                    player_parameters = line.split(',')
                    super().add_player(Player(player_parameters[0], player_parameters[1], player_parameters[2]))
        except Exception as e:
            print(e)

    def add_player(self, player):
        super(RepoTextFile, self).add_player(player)

    def update_players_strength(self, player_id, new_strength):
        super(RepoTextFile, self).update_players_strength(player_id, new_strength)
