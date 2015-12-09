from game import Game
def _integer_input(message):
    try:
        return int(raw_input(message))
    except StandardError:
        return _integer_input(message)

class CliInputter(object):
    def __init__(self):
        pass

    def next_move(self):
        board_index = _integer_input("Board? ")
        x = _integer_input("X Position? ")
        y = _integer_input("Y Position? ")

        return board_index, x, y
