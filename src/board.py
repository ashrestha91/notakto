from notakto_exceptions import InvalidMove

class Board(object):
    def __init__(self):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]

    def make_move(self, x, y):
        if self.board[x][y] != 1:
            self.board[x][y] = 1
        else:
            raise InvalidMove("Already moved in position ({},{})".format(x,y))

    def pos(self, x, y):
        return self.board[x][y]

    def get_valid_moves():
        raise NotImplementedError

    def is_alive(self):
        # columns
        columns_full = [ sum(col) == 3 for col in self.board ]
        if any(columns_full):
            return False

        # rows
        rows = []
        for y in range(0,2):
            row = [self.pos(0, y), self.pos(1, y), self.pos(2, y)]
            rows.append(row)

        rows_full = [ sum(row) == 3 for row in rows ]
        if any(rows_full):
            return False

        # diagonal
        diagonals = [ [self.pos(0,0), self.pos(1,1), self.pos(2,2)],
                      [self.pos(2,0), self.pos(1,1), self.pos(0,2)]]

        diagonals_full = [ sum(diagonal) == 3 for diagonal in diagonals ]
        if any(diagonals_full):
            return False

        return True
