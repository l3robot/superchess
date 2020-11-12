"""This file defines the mechanics of a game with an AI.
"""

import time

from IPython import display
from IPython.display import SVG

import chess
from chess import svg
from superchess.players import HumanPlayer, RandomPlayer, MinMaxPlayer, AlphaBetaPlayer

class NoDisplay():

    def render(self, board):
        pass

class JupyterDisplay():

    def __init__(self, delay):
        self.delay = delay

    def render(self, board):
        """This function clear and render the board in a jupyter cell
        output."""
        display.clear_output(wait=True)
        display.display(
            SVG(svg.board(board, size=400, lastmove=board.move_stack[-1] if board.move_stack != [] else None))
        )
        time.sleep(self.delay)

def create_gui(name, delay):
    if name is None:
        return NoDisplay()
    elif name.lower() == 'jupyter':
        return JupyterDisplay(delay)

def game_loop(player1, player2, board=None, gamelength=-1, delay=0, gui='jupyter'):
    """Play a game and return end board. Can render to different GUIs."""
    if board is None:
        board = chess.Board() # Create a new board.
    gui = create_gui(gui, delay)
    gui.render(board)

    count = 0
    while count != gamelength:

        # Player1 move.
        p1_move = player1.get_move(board)
        board.push(p1_move)
        gui.render(board)
        if board.is_game_over():
            res = board.result().split('-')[0]
            if res == '1/2':
                print('The game is a draw.')
            elif res == '1':
                print('White wins.')
            else:
                print('black wins')
            break

        # Player2 move.
        p2_move = player2.get_move(board)
        board.push(p2_move)
        gui.render(board)
        if board.is_game_over():
            res = board.result().split('-')[0]
            if res == '1/2':
                print('The game is a draw.')
            elif res == '1':
                print('White wins.')
            else:
                print('black wins')
            break

        count += 1
    return board

def play_game(opponent='alphabeta', color='white'):
    player1 = HumanPlayer()
    if opponent == 'random':
        player2 = RandomPlayer()
    elif opponent == 'minmax':
        player2 = MinMaxPlayer()
    elif opponent == 'alphabeta':
        player2 = AlphaBetaPlayer()
    else:
        raise ValueError("opponent must be one of 'random', 'minmax', or 'alphabeta'.")

    if color=="white":
        game_loop(player1, player2)
    else:
        game_loop(player2, player1)
