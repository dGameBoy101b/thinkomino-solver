from unittest import TestCase
from thinkomino_tiles_csv_loader import load_tiles_csv
from io import StringIO
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour

class ThinkominoTilesCSVLoaderTest(TestCase):

	def setUp(self):
		self.csv = StringIO()

	def tearDown(self):
		self.csv.close()

	def write_tiles(self, tiles: list[ThinkominoTile]) -> None:
		self.csv.writelines(map(lambda tile: f'{",".join(map(lambda colour: colour.value, tile))}\n', tiles))

	def test_load_none(self):
		self.assertEqual(load_tiles_csv(self.csv), list())

	def test_load_one(self):
		TILE = ThinkominoTile(
				ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, ThinkominoColour.RED,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		self.write_tiles([TILE])
		self.csv.seek(0)
		self.assertEqual(load_tiles_csv(self.csv), [TILE])

	def test_load_many(self):
		TILES = [
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE),
			ThinkominoTile(
				ThinkominoColour.RED, ThinkominoColour.PURPLE, ThinkominoColour.YELLOW,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.ORANGE),
			ThinkominoTile(
				ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, ThinkominoColour.RED,
				ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
		]
		self.write_tiles(TILES)
		self.csv.seek(0)
		self.assertEqual(load_tiles_csv(self.csv), TILES)
