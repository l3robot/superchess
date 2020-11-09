"""This module implements the mini-max algorithm."""

import random

import math
import chess

from .player import Player


VAL_DICT = {
    chess.QUEEN: 9,
    chess.ROOK: 5,
    chess.BISHOP: 3,
    chess.KNIGHT: 3,
    chess.PAWN: 1,
    chess.KING: 100
}


def score_board(board):
    score = 0
    for piece in board.piece_map().values():
        if piece.color == board.turn:
            score += VAL_DICT[piece.piece_type]
        else:
            score -= VAL_DICT[piece.piece_type]
    if board.is_checkmate():
        score -= 1000
    turn_mobility = board.legal_moves.count()
    board.turn = False if True else True
    other_mobility = board.mirror().legal_moves.count()
    board.turn = False if True else True
    score += 0.1 * (turn_mobility - other_mobility)

    if rel_score == False:
        score = score * (1 if board.turn else -1)
    return score


def rollout(board, depth=3, reduce="max"):
    board_copy = board.copy()
    best_score = 0 if reduce == "max" else math.inf
    mobility = board_copy.legal_moves.count()
    if not mobility:
        sign = -1 if reduce == "max" else 1
        return sign * 1000
    best_moves = [list(board_copy.legal_moves)[0]]
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


class MinMaxPlayer(Player):
    """Defines a Random Policy."""

    def __init__(self, rollout_depth=3):
        self.rollout_depth = rollout_depth

    def get_move(self, board):
        best_move = rollout(board, self.rollout_depth)[-1]
        return best_move
