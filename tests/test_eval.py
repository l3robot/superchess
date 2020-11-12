import unittest
import chess
import math
from superchess.eval import score_board_rel, score_board_abs

class TestScoreBoardRel(unittest.TestCase):
	"""This suite tests the relative score returned by score_board_rel."""
	def test_checkmate(self):
		"""Being checkmated should return a score of -inf, irrespective of color."""
		checkmatedblack = chess.Board(fen='k1Q5/8/K7/8/8/8/8/8 b')
		self.assertTrue(score_board_rel(checkmatedblack) == -math.inf)
		checkmatedwhite = checkmatedblack.mirror()
		self.assertTrue(score_board_rel(checkmatedwhite) == -math.inf)

	def test_stalemate(self):
		"""Stalemate position should return a score of 0 for both colors."""
		stalemateblack = chess.Board(fen='k7/8/K1N5/8/8/8/8/8 b')
		self.assertTrue(score_board_rel(stalemateblack) == 0)
		stalematewhite = stalemateblack.mirror()
		self.assertTrue(score_board_rel(stalematewhite) == 0)

	def test_winning(self):
		"""Winning position should have positive score, and score should be same for mirrored board."""
		winningwhite = chess.Board(fen='k7/8/K7/8/8/8/8/2R5 w')
		self.assertTrue(score_board_rel(winningwhite) > 0)
		winningblack = winningwhite.mirror()
		self.assertTrue(score_board_rel(winningblack) > 0)
		self.assertTrue(score_board_rel(winningwhite) == score_board_rel(winningblack))

class TestScoreBoardRel(unittest.TestCase):
	"""This suite tests the absolute score returned by score_board_abs."""
	def test_checkmate(self):
		"""Being checkmated should return a score of -inf, irrespective of color."""
		checkmatewhite = chess.Board(fen='k1Q5/8/K7/8/8/8/8/8 b')
		self.assertTrue(score_board_abs(checkmatewhite) == math.inf)
		checkmateblack = checkmatewhite.mirror()
		self.assertTrue(score_board_abs(checkmateblack) == -math.inf)

	def test_stalemate(self):
		"""Stalemate position should return a score of 0 for both colors."""
		stalemateblack = chess.Board(fen='k7/8/K1N5/8/8/8/8/8 b')
		self.assertTrue(score_board_rel(stalemateblack) == 0)
		stalematewhite = stalemateblack.mirror()
		self.assertTrue(score_board_rel(stalematewhite) == 0)

	def test_winning(self):
		"""Winning position should have positive score for white, negative for black."""
		winningwhite = chess.Board(fen='k7/8/K7/8/8/8/8/2R5 w')
		self.assertTrue(score_board_abs(winningwhite) > 0)
		winningblack = winningwhite.mirror()
		self.assertTrue(score_board_abs(winningblack) < 0)
		self.assertTrue(score_board_abs(winningwhite) == - score_board_abs(winningblack))

if __name__ == '__main__':
	unittest.main()