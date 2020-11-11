"""Module that contains search facilities."""
import math
import random
from superchess.eval import score_board

def rollout(board, depth=3, reduce="max"):
	board_copy = board.copy()
	best_score = -math.inf if reduce == "max" else math.inf
	best_moves = list(board_copy.legal_moves)[:1]
	for move in board_copy.legal_moves:
		board_copy.push(move)
		if depth == 1:
			sign = -1 if reduce == "max" else 1
			score = sign * score_board(board_copy)
		else:
			next_reduce = "min" if reduce == "max" else "max"
			score = rollout(board_copy, depth=depth - 1, reduce=next_reduce)[
				0
			]
		improving = (
			(score > best_score) if reduce == "max" else (score < best_score)
		)
		if improving:
			best_score = score
			best_moves = [move]
		elif score == best_score:
			best_moves.append(move)
		board_copy.pop()
	return best_score, random.choice(best_moves)