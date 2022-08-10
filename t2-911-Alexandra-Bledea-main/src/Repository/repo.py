from src.Domain.player import Player


class Repository:

    def __init__(self):
        self._players = []
        self.__load_file()

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value

    def __getitem__(self, item):
        return self._players[item]

    def get_player_by_id(self, player_id):
        player_exists = False
        for player in self._players:
            if player.player_id == player_id:
                player_exists = True

        if player_exists:
            return player
        else:
            return False

    def add_player(self, player):
        self._players.append(player)

    def update_players_strength(self, player_id, new_strength):
        player = self.get_player_by_id(player_id)
        player.strength = new_strength

    def __len__(self):
        return len(self._players)

    def __load_file(self):
        try:
            file = open("players.txt", 'rt')
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.strip('\n')
                if line == '':
                    continue
                else:
                    player_parameters = line.split(',')
                    self.add_player(Player(player_parameters[0], player_parameters[1], player_parameters[2]))
        except Exception as e:
            print(e)