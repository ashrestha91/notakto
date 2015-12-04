import unittest
from unittest import TestCase
from notakto_exceptions import InvalidMove
from board import Board

class BoardMoveTest(TestCase):
    def corner_test(self):
        board = Board()

        board.make_move(0,0)

        self.assertEqual(1, board.pos(0,0))
        self.assertEqual(0, board.pos(0,1))
        self.assertEqual(0, board.pos(1,0))

    def out_of_bounds_test(self):
        board = Board()

        with self.assertRaises(IndexError):
            board.make_move(2,4)

    def invalid_move_test(self):
        board = Board()

        board = Board()

        board.make_move(0,0)
        with self.assertRaises(InvalidMove):
            board.make_move(0,0)

class BoardGetValidMovesTest(TestCase):
    def remaining_moves():
        pass

class BoardIsAliveTests(TestCase):
    def living_test(self):
        board = Board()

        self.assertTrue(board.is_alive())

        board.make_move(0,0)
        self.assertTrue(board.is_alive())

    def column_test(self):
        board = Board()

        board.make_move(0,0)
        board.make_move(0,1)
        board.make_move(0,2)

        self.assertFalse(board.is_alive())

    def row_test(self):
        board = Board()

        board.make_move(0,0)
        board.make_move(1,0)
        board.make_move(2,0)

        self.assertFalse(board.is_alive())

    def diagonal_test(self):
        board = Board()

        board.make_move(0,0)
        board.make_move(1,1)
        board.make_move(2,2)

        self.assertFalse(board.is_alive())

