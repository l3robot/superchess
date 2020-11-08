"""This module defines the abstract player class interface."""
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_move(self, board):
        pass
