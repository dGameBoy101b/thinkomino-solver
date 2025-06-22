from unittest import TestCase
from thinkomino_board import ThinkominoBoard
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour
RED = ThinkominoColour.RED
ORANGE = ThinkominoColour.ORANGE
YELLOW = ThinkominoColour.YELLOW
GREEN = ThinkominoColour.GREEN
BLUE = ThinkominoColour.BLUE
PURPLE = ThinkominoColour.PURPLE

class ThinkominoBoardTest(TestCase):

	def test_initialisation(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		board = ThinkominoBoard(*TILES)
		self.assertIsInstance(board, ThinkominoBoard)
		self.assertEqual(board.north, TILES[0])
		self.assertEqual(board.north_west, TILES[1])
		self.assertEqual(board.south_west, TILES[2])
		self.assertEqual(board.south, TILES[3])
		self.assertEqual(board.south_east, TILES[4])
		self.assertEqual(board.north_east, TILES[5])

	def test_solve_check(self):
		self.assertFalse(ThinkominoBoard(
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None).is_solved())
		self.assertFalse(ThinkominoBoard(
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW)).is_solved())

	def test_representation(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		self.assertEqual(repr(ThinkominoBoard(*TILES)), f'ThinkominoBoard({", ".join(map(repr, TILES))!s})')

	def test_equality(self):
		TILES1 = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		self.assertTrue(ThinkominoBoard(*TILES1) == ThinkominoBoard(*TILES1))
		self.assertFalse(ThinkominoBoard(*TILES1) != ThinkominoBoard(*TILES1))
		TILES2 = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW))
		self.assertFalse(ThinkominoBoard(*TILES1) == ThinkominoBoard(*TILES2))
		self.assertTrue(ThinkominoBoard(*TILES1) != ThinkominoBoard(*TILES2))
		self.assertFalse(ThinkominoBoard(*TILES1) == TILES1)
		self.assertTrue(ThinkominoBoard(*TILES1) != TILES1)

	def test_hashing(self):
		TILES1 = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		self.assertEqual(hash(ThinkominoBoard(*TILES1)), hash(ThinkominoBoard(*TILES1)))
		TILES2 = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW))
		self.assertNotEqual(hash(ThinkominoBoard(*TILES1)), hash(ThinkominoBoard(*TILES2)))

	def test_shorthand_attributes(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		board = ThinkominoBoard(*TILES)
		self.assertEqual(board.n, TILES[0])
		self.assertEqual(board.nw, TILES[1])
		self.assertEqual(board.sw, TILES[2])
		self.assertEqual(board.s, TILES[3])
		self.assertEqual(board.se, TILES[4])
		self.assertEqual(board.ne, TILES[5])

	def test_indexing(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		board = ThinkominoBoard(*TILES)
		for index in range(-6, 6):
			self.assertEqual(board[index], TILES[index])
			self.assertEqual(board[:index], TILES[:index])
			self.assertEqual(board[index:], TILES[index:])

	def test_index_error(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		board = ThinkominoBoard(*TILES)
		with self.assertRaises(IndexError):
			board[6]
		with self.assertRaises(IndexError):
			board[-7]

	def test_mapping(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		board = ThinkominoBoard(*TILES)
		self.assertEqual(board['north'], TILES[0])
		self.assertEqual(board['n'], TILES[0])
		self.assertEqual(board[ThinkominoBoard.Direction.North], TILES[0])
		self.assertEqual(board['north west'], TILES[1])
		self.assertEqual(board['nw'], TILES[1])
		self.assertEqual(board[ThinkominoBoard.Direction.NorthWest], TILES[1])
		self.assertEqual(board['south west'], TILES[2])
		self.assertEqual(board['sw'], TILES[2])
		self.assertEqual(board[ThinkominoBoard.Direction.SouthWest], TILES[2])
		self.assertEqual(board['south'], TILES[3])
		self.assertEqual(board['s'], TILES[3])
		self.assertEqual(board[ThinkominoBoard.Direction.South], TILES[3])
		self.assertEqual(board['south east'], TILES[4])
		self.assertEqual(board['se'], TILES[4])
		self.assertEqual(board[ThinkominoBoard.Direction.SouthEast], TILES[4])
		self.assertEqual(board['north east'], TILES[5])
		self.assertEqual(board['ne'], TILES[5])
		self.assertEqual(board[ThinkominoBoard.Direction.NorthEast], TILES[5])

	def test_key_error(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			None,
			None,
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		board = ThinkominoBoard(*TILES)
		with self.assertRaises(KeyError):
			board['east']
		with self.assertRaises(KeyError):
			board['e']
		with self.assertRaises(KeyError):
			board['west']
		with self.assertRaises(KeyError):
			board['w']

	def test_iterable(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				PURPLE, BLUE, YELLOW,
				GREEN, ORANGE, RED),
			ThinkominoTile(
				ORANGE, BLUE, GREEN,
				YELLOW, PURPLE, RED),
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		iterator = iter(ThinkominoBoard(*TILES))
		self.assertEqual(next(iterator), TILES[0])
		self.assertEqual(next(iterator), TILES[1])
		self.assertEqual(next(iterator), TILES[2])
		self.assertEqual(next(iterator), TILES[3])
		self.assertEqual(next(iterator), TILES[4])
		self.assertEqual(next(iterator), TILES[5])
		with self.assertRaises(StopIteration):
			next(iterator)

	def test_membership_checking(self):
		TILES = (
			ThinkominoTile(
				RED, ORANGE, YELLOW,
				GREEN, BLUE, PURPLE),
			ThinkominoTile(
				BLUE, GREEN, ORANGE,
				PURPLE, RED, YELLOW),
			ThinkominoTile(
				PURPLE, BLUE, YELLOW,
				GREEN, ORANGE, RED),
			ThinkominoTile(
				ORANGE, BLUE, GREEN,
				YELLOW, PURPLE, RED),
			ThinkominoTile(
				PURPLE, BLUE, GREEN,
				YELLOW, ORANGE, RED),
			None)
		board = ThinkominoBoard(*TILES)
		for tile in TILES:
			self.assertTrue(tile in board)
		self.assertFalse(ThinkominoTile(
			PURPLE, BLUE, ORANGE,
			YELLOW, GREEN, RED) in board)
