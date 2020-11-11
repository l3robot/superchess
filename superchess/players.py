"""This module defines the players (humans or algorithms) that can participate in chess games."""
from abc import ABC, abstractmethod
import random
from superchess.search import rollout

class Player(ABC):
	"""Abstract class that defines the player interface."""
	def __init__(self):
		pass

	@abstractmethod
	def get_move(self, board):
		pass

class RandomPlayer(Player):
	"""Dumb player that plays random moves."""

	def get_move(self, board):
		return random.choice(list(board.legal_moves))

class HumanPlayer(Player):
	"""Ask a user to enter a move in a cli or jupyter notebook."""

	def get_move(self, board):
		while True:
			input_text = input("Enter a valid move (uci or san): ")
			try:
				move = board.parse_uci(input_text)
				break
			except ValueError:
				try:
					move = board.parse_san(input_text)
					break
				except ValueError:
					print("Not a valid move. Try again.")
		return move

class MinMaxPlayer(Player):
	"""Defines a minmax player that does tree-search without alpha-beta pruning."""

	def __init__(self, rollout_depth=3):
		self.rollout_depth = rollout_depth

	def get_move(self, board):
		best_move = rollout(board, self.rollout_depth)[-1]
		return best_move