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
            print "{} {} {}".format(board.pos(0, 0), board.pos(1,0), board.pos(2,0))
            print "{} {} {}".format(board.pos(0, 1), board.pos(1,1), board.pos(2,1))
            print "{} {} {}".format(board.pos(0, 2), board.pos(1,2), board.pos(2,2))
            print "==========="
        print

    def render_error(self, game, error):
        print
        print ">>>>>>"
        print ">> {} <<".format(error)
        print ">>>>>>"

        self.render(game)
