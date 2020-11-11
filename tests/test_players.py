import unittest
import chess
from superchess.players import MinMaxPlayer

class TestMinMaxPlayer(unittest.TestCase):
	"""This suite tests the MinMaxPlayer."""
	def setUp(self):
		self.minmax1 = MinMaxPlayer(rollout_depth=1)

	def test_finds_checkmatein1(self):
		checkmatein1board = chess.Board(fen='k7/8/K7/8/8/8/8/2R5 w')
		self.assertTrue(self.minmax1.get_move(checkmatein1board) == checkmatein1board.parse_san('Rc8'))



if __name__ == '__main__':
	unittest.main()