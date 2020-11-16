import sys
from PySide2 import QtSvg
from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Slot, QTimer, SIGNAL
import PySide2.QtGui as QtGui
import chess
import chess.svg
from superchess.players import AlphaBetaPlayer
import time
import random

def board2bytes(board):
	svgboard = chess.svg.board(board)
	svgbytesboard = bytearray(svgboard, encoding='utf-8')
	return svgbytesboard

def xy2square(x,y):
	WIDTH=45
	breakpoints = [15+WIDTH*i for i in range(1,9)]
	xs = ['a','b','c','d','e','f','g','h']
	ys = ['8','7','6','5','4','3','2','1']
	squarestr = ""
	for i,bp in enumerate(breakpoints):
		if x<bp:
			squarestr += xs[i]
			break
	for i,bp in enumerate(breakpoints):
		if y<bp:
			squarestr += ys[i]
			break
	return squarestr

class svgWidget(QtSvg.QSvgWidget):
	def __init__(self, opponent):
		super().__init__()
		self.opponent = opponent

		self.board = chess.Board()
		self.moveuci = ""

		self.renderer().load(board2bytes(self.board))
		self.show()

		timer = QTimer(self)
		timer.timeout.connect(self.opponentmove)
		timer.start(100)

	def mousePressEvent(self, e):
		self.moveuci = xy2square(e.x(), e.y())

	def mouseReleaseEvent(self, e):
		self.moveuci += xy2square(e.x(), e.y())
		try:
			move = self.board.parse_uci(self.moveuci)
		except ValueError:
			pass
		else:
			self.board.push(move)
			self.renderer().load(board2bytes(self.board))

	def opponentmove(self):
		# This is a hack. this should be at the end of mouseReleaseEvent,
		# but then it only updates the screen with both white and black moves...
		# there should be a way to render the screen after white's move, but I dont know how
		if self.board.turn == False:
			opponent_move = self.opponent.get_move(self.board)
			self.board.push(opponent_move)
			self.renderer().load(board2bytes(self.board))

		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	opponent = AlphaBetaPlayer()
	gw = svgWidget(opponent)
	app.exec_()
