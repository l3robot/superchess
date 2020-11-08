"""This file defines the mechanics of a game with an AI.
"""

import time

from IPython import display
from IPython.display import SVG

import chess
from chess import svg


def render_in_jupyter(board):
    """This function clear and render the board in a jupyter cell
    output."""
    display.clear_output(wait=True)
    display.display(
        SVG(svg.board(board, size=300, lastmove=board.move_stack[-1] if board.move_stack != [] else None))
    )


def main_jupyter_loop(player1, player2, gamelength=-1, delay=1):
    """Create a very simple game loop for jupyter notebook."""
    board = chess.Board() # Create a new board.
    count = 0
    while count != gamelength:
        # Render.
        render_in_jupyter(board)
        # Player1 move.
        p1_move = player1.get_move(board)
        board.push(p1_move)
        if board.is_game_over():
            res = board.result().split('-')[0]
            if res == '1/2':
                print('The game is a draw.')
            elif res == '1':
                print('White wins.')
            else:
                print('black wins')
            break
        # Sleep.
        time.sleep(delay)
        # Render.
        render_in_jupyter(board)
        # Player2 move.
        p2_move = player2.get_move(board)
        board.push(p2_move)
        if board.is_game_over():
            res = board.result().split('-')[0]
            if res == '1/2':
                print('The game is a draw.')
            elif res == '1':
                print('White wins.')
            else:
                print('black wins')
            break
        # Sleep.
        time.sleep(delay)
        count += 1
