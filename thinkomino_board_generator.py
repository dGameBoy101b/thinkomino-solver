from typing import Iterator
from thinkomino_board import ThinkominoBoard
from thinkomino_tile import ThinkominoTile
from list_permuter import permute_list, Permutations
from list_rotator import Rotations

def permute_rotations(tiles: list[ThinkominoTile]) -> list[ThinkominoTile]:
	if len(tiles) < 2:
		yield tiles
		return
	for rotation in Rotations(tiles[0]):
		for permutation in permute_rotations(tiles[1:]):
			yield [ThinkominoTile(*rotation)] + permutation

def generate_boards(tiles: list[ThinkominoTile]) -> Iterator[ThinkominoBoard]:
	for ordered_tiles in permute_list(tiles):
		for state in permute_rotations(ordered_tiles):
			yield ThinkominoBoard(*state)

class BoardGenerator(Iterator[ThinkominoBoard]):
	def __init__(self, tiles:tuple[ThinkominoTile]):
		self.__orderer = Permutations(tiles)
		self.__ordered_tiles = None
		self.__rotators = list()

	def __iter__(self):
		return self
	
	def __next__(self)->ThinkominoBoard:
		if self.__ordered_tiles is None:
			try:
				self.__ordered_tiles = next(self.__orderer)
			except StopIteration:
				self.__rotators = None
				self.__orderer = None
				raise StopIteration
			self.__rotators = (Rotations(tile) for tile in self.__ordered_tiles)
			

	def __len__(self)->int:
