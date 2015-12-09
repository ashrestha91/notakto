import unittest
from unittest import TestCase
from notakto_exceptions import InvalidMove
from game import Game

class GameInitTest(TestCase):
    def starts_with_n_boards_test(self):
        game = Game(2)
        self.assertEquals(2, len(game.boards))

    def fails_with_illegal_arguments_test(self):
        with self.assertRaises(ValueError):
            game = Game(0)

class GameLivingBoardsTest(TestCase):
    def all_boards_alive_test(self):
        game = Game(2)
        self.assertEquals(2, len(game.living_boards()))

    def does_not_return_dead_boards_test(self):
        game = Game(2)

        living_board = game.boards[1]

        board = game.boards[0]
        board.make_move(0,0)
        board.make_move(1,0)
        board.make_move(2,0)

        self.assertEquals(1, len(game.living_boards()))
        self.assertEquals(living_board, game.living_boards()[0])

class GameMakeMove(TestCase):
    def applies_to_correct_board_test(self):
        game = Game(2)

        game.make_move(0, 1, 1)
        self.assertEquals(1, game.boards[0].pos(1,1))
        self.assertEquals(0, game.boards[1].pos(1,1))

    def raises_error_on_dead_boards_test(self):
        game = Game(2)

        game.make_move(0, 1, 0)
        game.make_move(0, 1, 1)
        game.make_move(0, 1, 2)
        with self.assertRaises(InvalidMove):
            game.make_move(0, 0, 0)

class GameIsOver(TestCase):
    def game_ongoing(self):
        game = Game(1)
        self.assertFalse(game.is_over())

    def end_game_test(self):
        game = Game(1)

        game.make_move(0, 1, 0)
        game.make_move(0, 1, 1)
        game.make_move(0, 1, 2)

        self.assertTrue(game.is_over())
