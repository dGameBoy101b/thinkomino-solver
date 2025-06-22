from unittest import TestCase
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour

class ThinkominoTileTest(TestCase):

	def test_initialisation(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		tile = ThinkominoTile(*COLOURS)
		self.assertIsInstance(tile, ThinkominoTile)
		self.assertEqual(tile.east, COLOURS[0])
		self.assertEqual(tile.north_east, COLOURS[1])
		self.assertEqual(tile.north_west, COLOURS[2])
		self.assertEqual(tile.west, COLOURS[3])
		self.assertEqual(tile.south_west, COLOURS[4])
		self.assertEqual(tile.south_east, COLOURS[5])

	def test_value_error(self):
		with self.assertRaises(ValueError):
			ThinkominoTile(1,2,3,4,5,6)
		with self.assertRaises(ValueError):
			ThinkominoTile('red','orange', 'yellow','green','blue','purple')
		with self.assertRaises(ValueError):
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
				ThinkominoColour.GREEN, ThinkominoColour.YELLOW, ThinkominoColour.PURPLE)
		with self.assertRaises(ValueError):
			ThinkominoTile(None, None, None, None, None, None)

	def test_indexing(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		tile = ThinkominoTile(*COLOURS)
		for index in range(-6, 6):
			self.assertEqual(tile[index], COLOURS[index])
			self.assertEqual(tile[index:], COLOURS[index:])
			self.assertEqual(tile[:index], COLOURS[:index])

	def test_index_error(self):
		with self.assertRaises(IndexError):
			ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)[6]
		with self.assertRaises(IndexError):
			ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)[-7]

	def test_shorthand_attributes(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		tile = ThinkominoTile(*COLOURS)
		self.assertEqual(tile.e, COLOURS[0])
		self.assertEqual(tile.ne, COLOURS[1])
		self.assertEqual(tile.nw, COLOURS[2])
		self.assertEqual(tile.w, COLOURS[3])
		self.assertEqual(tile.sw, COLOURS[4])
		self.assertEqual(tile.se, COLOURS[5])

	def test_attribute_error(self):
		with self.assertRaises(AttributeError):
			ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE).north
		with self.assertRaises(AttributeError):
			ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE).south
		with self.assertRaises(AttributeError):
			ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE).n
		with self.assertRaises(AttributeError):
			ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE).s

	def test_membership_checking(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		tile = ThinkominoTile(*COLOURS)
		for colour in COLOURS:
			self.assertTrue(colour in tile)
		self.assertFalse(None in tile)
		self.assertFalse(True in tile)
		self.assertFalse(1 in tile)
		self.assertFalse('a' in tile)
		self.assertFalse([] in tile)

	def test_iterable(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		iterator = iter(ThinkominoTile(*COLOURS))
		self.assertEqual(next(iterator), COLOURS[0])
		self.assertEqual(next(iterator), COLOURS[1])
		self.assertEqual(next(iterator), COLOURS[2])
		self.assertEqual(next(iterator), COLOURS[3])
		self.assertEqual(next(iterator), COLOURS[4])
		self.assertEqual(next(iterator), COLOURS[5])
		with self.assertRaises(StopIteration):
			next(iterator)

	def test_length(self):
		self.assertEqual(len(ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)), 6)

	def test_representation(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		self.assertEqual(repr(ThinkominoTile(*COLOURS)), 'ThinkominoTile(' + ', '.join(map(repr, COLOURS)) + ')')

	def test_equality(self):
		COLOURS1 = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		self.assertTrue(ThinkominoTile(*COLOURS1) == ThinkominoTile(*COLOURS1))
		self.assertFalse(ThinkominoTile(*COLOURS1) != ThinkominoTile(*COLOURS1))
		COLOURS2 = ( 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE,
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW)
		self.assertFalse(ThinkominoTile(*COLOURS1) == ThinkominoTile(*COLOURS2))
		self.assertTrue(ThinkominoTile(*COLOURS1) != ThinkominoTile(*COLOURS2))
		self.assertFalse(ThinkominoTile(*COLOURS1) == COLOURS1)
		self.assertTrue(ThinkominoTile(*COLOURS1) != COLOURS1)

	def test_mapping(self):
		COLOURS = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		tile = ThinkominoTile(*COLOURS)
		self.assertEqual(tile['east'], COLOURS[0])
		self.assertEqual(tile['north east'], COLOURS[1])
		self.assertEqual(tile['north west'], COLOURS[2])
		self.assertEqual(tile['west'], COLOURS[3])
		self.assertEqual(tile['south west'], COLOURS[4])
		self.assertEqual(tile['south east'], COLOURS[5])
		self.assertEqual(tile['e'], COLOURS[0])
		self.assertEqual(tile['ne'], COLOURS[1])
		self.assertEqual(tile['nw'], COLOURS[2])
		self.assertEqual(tile['w'], COLOURS[3])
		self.assertEqual(tile['sw'], COLOURS[4])
		self.assertEqual(tile['se'], COLOURS[5])
		self.assertEqual(tile[ThinkominoTile.Direction.East], COLOURS[0])
		self.assertEqual(tile[ThinkominoTile.Direction.NorthEast], COLOURS[1])
		self.assertEqual(tile[ThinkominoTile.Direction.NorthWest], COLOURS[2])
		self.assertEqual(tile[ThinkominoTile.Direction.West], COLOURS[3])
		self.assertEqual(tile[ThinkominoTile.Direction.SouthWest], COLOURS[4])
		self.assertEqual(tile[ThinkominoTile.Direction.SouthEast], COLOURS[5])

	def test_hashing(self):
		COLOURS1 = (
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		self.assertEqual(hash(ThinkominoTile(*COLOURS1)), hash(ThinkominoTile(*COLOURS1)))
		COLOURS2 = ( 
			ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE,
			ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW)
		self.assertNotEqual(hash(ThinkominoTile(*COLOURS1)), hash(ThinkominoTile(*COLOURS2)))
