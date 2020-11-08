"""Dumb player that plays random moves."""
from players.player import Player
import random


class RandomPlayer(Player):
    """Defines a Random Policy."""

    def get_move(self, board):
        return random.choice(list(board.legal_moves))
