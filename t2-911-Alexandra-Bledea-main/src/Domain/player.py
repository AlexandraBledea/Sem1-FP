

class Player:

    def __init__(self, player_id, name, strength):
        self._player_id = player_id
        self._name = name
        self._strength = strength

    @property
    def player_id(self):
        return self._player_id

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    def __str__(self):
        return str(self._player_id) + ' ' + str(self._name) + ' ' + str(self._strength)
