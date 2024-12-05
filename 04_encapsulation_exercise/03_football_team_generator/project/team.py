from typing import List
from project.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    def add_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} has already joined"

        self.players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str:
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
            self.players.remove(player)
            return player

        except StopIteration:
            return f"Player {player_name} not found"
