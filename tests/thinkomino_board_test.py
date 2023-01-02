from unittest import TestCase
from thinkomino_board import ThinkominoBoard
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour

class ThinkominoBoardTest(TestCase):

	def test_valid_boards(self):
		TILES = (
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE),
			ThinkominoTile(
				ThinkominoColour.BLUE, ThinkominoColour.GREEN, ThinkominoColour.ORANGE,
				ThinkominoColour.PURPLE, ThinkominoColour.RED, ThinkominoColour.YELLOW),
			None,
			None,
			ThinkominoTile(
				ThinkominoColour.PURPLE, ThinkominoColour.BLUE, ThinkominoColour.GREEN,
				ThinkominoColour.YELLOW, ThinkominoColour.ORANGE, ThinkominoColour.RED),
			None)
		board = ThinkominoBoard(TILES)
		self.assertIsInstance(board, ThinkominoBoard)
		self.assertSequenceEqual(board, TILES)

	def test_solve_check(self):
		board = ThinkominoBoard([
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE),
			ThinkominoTile(
				ThinkominoColour.BLUE, ThinkominoColour.GREEN, ThinkominoColour.ORANGE,
				ThinkominoColour.PURPLE, ThinkominoColour.RED, ThinkominoColour.YELLOW),
			None,
			None,
			ThinkominoTile(
				ThinkominoColour.PURPLE, ThinkominoColour.BLUE, ThinkominoColour.GREEN,
				ThinkominoColour.YELLOW, ThinkominoColour.ORANGE, ThinkominoColour.RED),
			None])
		self.assertFalse(board.is_solved())
