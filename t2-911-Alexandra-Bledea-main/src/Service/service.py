from src.Repository.repo import Repository
import random


class Service:

    def __init__(self):
        self._repository = Repository()
        self.sort_players()
        self.made_pairs = []

    def check_qualifications(self):
        """
        With this function we check if there is need of a qualification
        :return:
        """
        length = len(self._repository.players)
        return length != 0 and (length and (length - 1) == 0)

    def qualifications(self):
        """
        With this function we compute the players up for the qualifications
        :return:
        """
        length = len(self._repository.players)
        powers = self.powers_of_two(length)
        required_matches = length - powers[-1]
        number_of_players = 2*required_matches
        start_position = length - number_of_players
        qualification_players = []
        for i in range(start_position, len(self._repository.players)):
            qualification_players.append(self._repository.players[i])
        return qualification_players

    def choose_random_the_pairs(self, players_list):
        """
        With this function we pair the players randomly
        :param players_list: the list with the players we should pair randomly
        :return: it returns the made pair
        """
        ok = 0
        made_players = []
        while ok != 2:
            player = players_list[random.randint(0, len(players_list))-1]
            if player not in self.made_pairs:
                made_players.append(player)
                self.made_pairs.append(player)
                ok = ok + 1
        return made_players

    def powers_of_two(self, length):
        """
        With this function we calculate the length in power of 2
        :param length:
        :return:
        """
        powers = []
        i = 1
        while i <= length:
            if i & length:
                powers.append(i)
            i <<= 1
        return powers

    def sort_players(self):
        self._repository.players.sort(reverse=True, key=lambda x: x.strength)