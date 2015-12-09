from game import Game
from board import Board
from notakto_exceptions import InvalidMove

class GameRunner(object):
    def __init__(self, game, renderer, inputter):
        self.game = game
        self.renderer = renderer
        self.inputter = inputter

    def run(self):
        self.renderer.render(self.game)

        while not self.game.is_over():
            board_index, x, y = self.inputter.next_move()
            try:
                self.game.make_move(board_index, x, y)
                self.renderer.render(self.game)
            except InvalidMove as e:
                self.renderer.render_error(self.game, e.message)

