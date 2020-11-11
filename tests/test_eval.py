import unittest
import chess
from superchess.eval import score_board

class TestScoreBoardRel(unittest.TestCase):
	"""This suite tests the default relative score returned by score_board."""
	def test_checkmate(self):
		"""Being checkmated should return a score of -1000, irrespective of color."""
		checkmateblack = chess.Board(fen='k1Q5/8/K7/8/8/8/8/8 b')
		self.assertTrue(score_board(checkmateblack) == -1000)
		checkmatewhite = checkmateblack.mirror()
		self.assertTrue(score_board(checkmatewhite) == -1000)

	def test_stalemate(self):
		"""Stalemate position should return a score of 0 for both colors."""
		stalemateblack = chess.Board(fen='k7/8/K1N5/8/8/8/8/8 b')
		self.assertTrue(score_board(stalemateblack) == 0)
		stalematewhite = stalemateblack.mirror()
		self.assertTrue(score_board(stalematewhite) == 0)

	def test_winning(self):
		"""Winning position should have positive score, and score should be same for mirrored board."""
		winningwhite = chess.Board(fen='k7/8/K7/8/8/8/8/2R5 w')
		self.assertTrue(score_board(winningwhite) > 0)
		winningblack = winningwhite.mirror()
		self.assertTrue(score_board(winningblack) > 0)
		self.assertTrue(score_board(winningwhite) == score_board(winningblack))


if __name__ == '__main__':
	unittest.main()