from unittest import TestCase
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour

class ThinkominoTileTest(TestCase):

	def test_valid_tiles(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		list_tile = ThinkominoTile(list(COLOURS))
		self.assertIsInstance(list_tile, ThinkominoTile)
		self.assertSequenceEqual(list_tile, COLOURS)

		tuple_tile = ThinkominoTile(tuple(COLOURS))
		self.assertIsInstance(tuple_tile, ThinkominoTile)
		self.assertSequenceEqual(tuple_tile, COLOURS)

		set_tile = ThinkominoTile(set(COLOURS))
		self.assertIsInstance(set_tile, ThinkominoTile)
		self.assertCountEqual(set_tile, COLOURS)

	def test_length_error(self):
		with self.assertRaises(IndexError):
			ThinkominoTile([])
		with self.assertRaises(IndexError):
			ThinkominoTile([
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE,
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE])

	def test_value_error(self):
		with self.assertRaises(ValueError):
			ThinkominoTile([1,2,3,4,5,6])
		with self.assertRaises(ValueError):
			ThinkominoTile(['red','orange', 'yellow','green','blue','purple'])
		with self.assertRaises(ValueError):
			ThinkominoTile([
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
				ThinkominoColour.GREEN, ThinkominoColour.YELLOW, ThinkominoColour.PURPLE])
		with self.assertRaises(ValueError):
			ThinkominoTile([None, None, None, None, None, None])

	def test_type_error(self):
		with self.assertRaises(TypeError):
			ThinkominoTile(123456)
		with self.assertRaises(TypeError):
			ThinkominoTile(None)

	def test_indexing(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		tile = ThinkominoTile(COLOURS)
		for index in range(6):
			self.assertEqual(tile[index], COLOURS[index])
			self.assertEqual(tile[index:], COLOURS[index:])
			self.assertEqual(tile[:index], COLOURS[:index])
