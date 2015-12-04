from board import Board
from notakto_exceptions import InvalidMove

class Game(object):
    def __init__(self, n_boards):
        if n_boards < 1:
            raise ValueError("Must have at least 1 board")
        self._boards = []

        for i in range(n_boards):
            self._boards.append(Board())

    @property
    def boards(self):
        return self._boards

    def living_boards(self):
        return filter(lambda board: board.is_alive(), self.boards)

    def make_move(self, board_index, x, y):
        board = self.boards[board_index]
        if board.is_alive():
            board.make_move(x,y)
        else:
            raise InvalidMove("Board is already dead")

    def is_over(self):
        return not any(self.living_boards())
