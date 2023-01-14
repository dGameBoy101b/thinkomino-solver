from unittest import TestCase
from thinkomino_board_generator import generate_boards
from thinkomino_board import ThinkominoBoard
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour
from list_rotator import rotate_list
from list_permuter import permute_list

class ThinkominoBoardGeneratorTest(TestCase):

	def setUp(self):
		self.tiles = [
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE),
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.PURPLE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.ORANGE),
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE),
			ThinkominoTile(
				ThinkominoColour.BLUE, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.RED, ThinkominoColour.PURPLE),
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.GREEN, ThinkominoColour.YELLOW,
				ThinkominoColour.ORANGE, ThinkominoColour.BLUE, ThinkominoColour.PURPLE),
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.PURPLE,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.YELLOW)]
		self.generator = generate_boards(self.tiles)

	def __getattr__(self, name: str):
		if name == 'board':
			return ThinkominoBoard(*self.tiles)
		raise AttributeError

	def rotate_tile(self, tile_index: int, rotations: int = 1) -> None:
		generator = rotate_list([colour for colour in self.tiles[tile_index]], rotations, 2)
		next(generator)
		self.tiles[tile_index] = ThinkominoTile(*next(generator))

	def skip_generations(self, to_skip: int = 1) -> None:
		for i in range(to_skip):
			next(self.generator)

	def generate_rotations(self) -> None:
		for n in range(6**6):
			for i in reversed(range(6)):
				if (n % 6**i) == 0:
					self.rotate_tile(i)
			yield

	def generate_permutations(self) -> None:
		for board in permute_list(self.tiles):
			self.tiles = board
			yield

	def test_first_noop(self):
		self.assertEqual(next(self.generator), self.board)

	def test_first_rotation(self):
		self.skip_generations(1)
		for i in range(6):
			self.rotate_tile(5)
			self.assertEqual(next(self.generator), self.board)

	def test_first_set_rotations(self):
		for board in self.generate_rotations():
			self.assertEqual(next(self.generator), self.board)

	def test_first_rearrangement(self):
		next(self.generate_permutations())
		next(self.generate_permutations())
		self.skip_generations(6**6)
		for board in self.generate_rotations():
			self.assertEqual(next(self.generator), self.board)

	def test_all_rearrangements(self):
		for board in self.generate_permutations():
			self.assertEqual(next(self.generator), self.board)
			self.skip_generations(6**6)
