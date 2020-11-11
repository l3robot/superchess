"""Module that contains facilities to evaluate board positions."""
import chess

VAL_DICT = {
	chess.QUEEN: 9,
	chess.ROOK: 5,
	chess.BISHOP: 3,
	chess.KNIGHT: 3,
	chess.PAWN: 1,
	chess.KING: 100
}

def score_board(board, rel_score=True):
	"""Score the current board position.

	With rel_score=True, score relative to who's turn it is.
	Score is positive if the player whose turn it is is winning, and negative otherwise.

	With rel_score=False, use absolute score.
	Score is positive if white player is winning, and negative if black player is winning."""
	score = 0
	if board.is_checkmate():
		score -= 1000
	elif board.is_stalemate():
		pass
	else:
		for piece in board.piece_map().values():
			score += VAL_DICT[piece.piece_type] * (1 if piece.color==board.turn else -1)
		turn_mobility = board.legal_moves.count()
		board.turn = False if board.turn is True else True
		other_mobility = board.mirror().legal_moves.count()
		board.turn = False if board.turn is True else True
		score += 0.1 * (turn_mobility - other_mobility)

	if rel_score is False: # return absolute score
		score = score * (1 if board.turn else -1)
	return score