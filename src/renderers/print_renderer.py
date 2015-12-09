from game import Game
from board import Board

class PrintRenderer(object):
    def __init__(self):
        pass

    def render(self, game):
        print
        for i, board in enumerate(game.boards):
            print "Board {}".format(i)
            if not board.is_alive():
                print "DEAD BOARD"
            print "{}|{}|{}".format(self._render_cell(board.pos(0, 0)),
                    self._render_cell(board.pos(1,0)), 
                    self._render_cell(board.pos(2,0)))
            print  "-----------"
            print "{}|{}|{}".format(self._render_cell(board.pos(0, 1)), 
                    self._render_cell(board.pos(1,1)), 
                    self._render_cell(board.pos(2,1)))
            print  "-----------"
            print "{}|{}|{}".format(self._render_cell(board.pos(0, 2)), 
                    self._render_cell(board.pos(1,2)),
                    self._render_cell(board.pos(2,2)))
            print "==============="
        print

    def render_error(self, game, error):
        print
        print ">>>>>>"
        print ">> {} <<".format(error)
        print ">>>>>>"

        self.render(game)

    def _render_cell(self, pos_val):
        if pos_val == 0:
            return "   "
        else:
            return " X "
