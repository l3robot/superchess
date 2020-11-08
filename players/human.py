"""Human player for cli or jupyter."""
from players.player import Player


class HumanPlayer(Player):
    """Ask a user to enter a move in a cli or jupyter notebook."""

    def get_move(self, board):
        while True:
            input_text = input("Enter a valid move (uci or san): ")
            try:
                move = board.parse_uci(input_text)
                break
            except ValueError:
                try:
                    move = board.parse_san(input_text)
                    break
                except ValueError:
                    print("Not a valid move. Try again.")
        return move