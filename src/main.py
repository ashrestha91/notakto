from game import Game
from game_runner import GameRunner
from renderers.print_renderer import PrintRenderer
from inputters.cli_inputter import CliInputter

def main():
    game = Game(3)
    renderer = PrintRenderer()
    inputter = CliInputter()
    runner = GameRunner(game, renderer, inputter)
    runner.run()

if __name__ == "__main__":
    main()
