"""This file defines the mechanics of a game with an AI.
"""

import time

from IPython import display
from IPython.display import SVG

import chess
from chess import svg


def execute_human_move(board, uci_human_move):
    """Move a piece on a board from a human uci move."""
    # Truncate move to 4 char.
    uci_human_move = uci_human_move[:4]
    try:
        move = chess.Move.from_uci(uci_human_move)
        if move in board.legal_moves:
            board.push(move)
        else:
            raise ValueError
    except ValueError:
        print(f"Move {uci_human_move} is not valid")
        raise ValueError


def render_in_jupyter(board):
    """This function clear and render the board in a jupyter cell
    output."""
    display.clear_output(wait=True)
    display.display(
        SVG(svg.board(board, size=300, lastmove=board.move_stack[-1]))
    )


def main_jupyter_loop(player1, player2, delay=1):
    """Create a very simple game loop for jupyter notebook."""
    # Create a new board.
    board = chess.Board()
    while True:
        # Render.
        render_in_jupyter(board)
        # Player1 move.
        p1_move = player1.move()
        board.push(p1_move)
        # Render.
        render_in_jupyter(board)
        # Player2 move.
        p2_move = player2.move()
        board.push(p2_move)
        # Sleep.
        time.sleep(delay)
