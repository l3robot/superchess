import unittest
import chess
from superchess.players import MinMaxPlayer, AlphaBetaPlayer
from superchess.game_mechanics import play_game

class TestMinMaxPlayer(unittest.TestCase):
	"""This suite tests the MinMaxPlayer."""
	def setUp(self):
		self.minmax1 = MinMaxPlayer(rollout_depth=1)
		self.minmax2 = MinMaxPlayer(rollout_depth=2)
		self.minmax3 = MinMaxPlayer(rollout_depth=3)

	def test_checkmatein1(self):
		checkmatein1board = chess.Board(fen='k7/8/K7/8/8/8/8/2R5 w')
		self.assertTrue(self.minmax1.get_move(checkmatein1board) == checkmatein1board.parse_san('Rc8'))
		self.assertTrue(self.minmax2.get_move(checkmatein1board) == checkmatein1board.parse_san('Rc8'))
		self.assertTrue(self.minmax3.get_move(checkmatein1board) == checkmatein1board.parse_san('Rc8'))

	def test_checkmatein2_rooks(self):
		checkmatein2board = chess.Board(fen='8/k7/6R1/8/8/8/8/K6R w')
		endboard = play_game(self.minmax3, self.minmax1, checkmatein2board, gamelength=2, delay=1, gui=None)
		self.assertTrue(endboard.is_game_over() == True)

	def test_minmax3_finds_quickest_checkmate(self):
		"""There are checkmates in 3, but we want minmax3 to find the checkmate in 1."""
		checkmatein1board = chess.Board(fen='k7/6R1/8/8/8/8/8/K6R w')
		self.assertTrue(self.minmax3.get_move(checkmatein1board) == checkmatein1board.parse_san('Rh8'))

class TestAlphaBetaPlayer(unittest.TestCase):
	"""This suite tests the MinMaxPlayer."""
	def setUp(self):
		self.alphabeta1 = AlphaBetaPlayer(rollout_depth=1)
		self.alphabeta2 = AlphaBetaPlayer(rollout_depth=2)
		self.alphabeta3 = AlphaBetaPlayer(rollout_depth=3)

	def test_checkmatein1_rook(self):
		checkmatein1board = chess.Board(fen='k7/8/K7/8/8/8/8/2R5 w')
		self.assertTrue(self.alphabeta1.get_move(checkmatein1board) == checkmatein1board.parse_san('Rc8'))
		self.assertTrue(self.alphabeta2.get_move(checkmatein1board) == checkmatein1board.parse_san('Rc8'))
		self.assertTrue(self.alphabeta3.get_move(checkmatein1board) == checkmatein1board.parse_san('Rc8'))

	def test_checkmatein1_queen(self):
		checkmatein1board = chess.Board('1k6/8/K7/8/4Q3/8/8/8')
		#self.assertTrue(self.alphabeta1.get_move(checkmatein1board) == checkmatein1board.parse_san('Qb7'))
		#self.assertTrue(self.alphabeta2.get_move(checkmatein1board) == checkmatein1board.parse_san('Qb7'))
		self.assertTrue(self.alphabeta3.get_move(checkmatein1board) == checkmatein1board.parse_san('Qb7'))

	def test_checkmatein2_rooks(self):
		checkmatein2board = chess.Board(fen='8/k7/6R1/8/8/8/8/K6R w')
		endboard = play_game(self.alphabeta3, self.alphabeta1, checkmatein2board, gamelength=2, delay=1, gui=None)
		self.assertTrue(endboard.is_game_over() == True)


if __name__ == '__main__':
	unittest.main()