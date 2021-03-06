"""Module that contains search facilities."""
import math
import random
import chess
from superchess.eval import score_board_rel, score_board_abs

def minmax_treesearch(board, depth=3, reduce="max"):
	# TODO: there's still a bug in here somewhere...
	if depth == 0 or board.is_game_over():
		return score_board_rel(board), depth, []
	best_score = -math.inf if reduce == "max" else math.inf
	smallest_depth = 0 # depth counts backwards so confusing
	best_moves = []
	for move in board.legal_moves:
		board.push(move)
		next_reduce = "min" if reduce == "max" else "max"
		score,dbt,_ = minmax_treesearch(board, depth=depth - 1, reduce=next_reduce)
		score = - score # using relative score and want score from our perspective
		improving = (
			(score > best_score) if reduce == "max" else (score < best_score)
		)
		if improving or score==best_score and dbt>smallest_depth:
			best_score = score
			best_moves = [move]
			smallest_depth = dbt
		elif score == best_score and dbt==smallest_depth:
			best_moves.append(move)
		board.pop()
	if best_moves == []:
		raise Exception("No available move")
	return best_score, smallest_depth, best_moves

def alphabeta(board, depth, alpha, beta, reduce="max", use_mobility=False):
	# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
	# Started with this pseudocode but added smallest_depth to give priority to
	# game-ending moves in case of ties.
	if depth == 0 or board.is_game_over():
		return score_board_abs(board, use_mobility=use_mobility), depth, []
	best_score = -math.inf if reduce=="max" else math.inf
	smallest_depth = 0 # depth counts backwards so confusing
	best_moves = []
	for move in board.legal_moves:
		board.push(move)
		if reduce=="max":
			score, dbt, _ = alphabeta(board, depth-1, alpha, beta, "min")
			if score > best_score or score==best_score and dbt > smallest_depth:
				best_score = score
				best_moves = [move]
				smallest_depth = dbt
				alpha = score
				if alpha > beta:
					board.pop()
					break
			elif score == best_score and dbt==smallest_depth:
				best_moves.append(move)
		elif reduce=="min":
			score, dbt, _ = alphabeta(board, depth-1, alpha, beta, "max")
			if score < best_score or score==best_score and dbt > smallest_depth:
				best_score = score
				best_moves = [move]
				smallest_depth = dbt
				beta = score
				if beta < alpha:
					board.pop()
					break
			elif score == best_score and dbt==smallest_depth:
				best_moves.append(move)
		board.pop()
	return best_score, smallest_depth, best_moves
		

def alphabeta_treesearch(board, depth=3, use_mobility=False):
	# alpha is the lowerbound for maximizers so set to -infinity
	# beta is the upper bound for minimizers so set to infinity
	reduce = "max" if board.turn else "min" # white players maxs, black mins
	score, dbt, moves = alphabeta(board, depth, -math.inf, math.inf, use_mobility=use_mobility, reduce=reduce)
	return score, depth-dbt, moves