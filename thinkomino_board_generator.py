from typing import Iterator
from thinkomino_board import ThinkominoBoard
from thinkomino_tile import ThinkominoTile
from list_permuter import Permutations
from rotation_combiner import Rotateable, RotationCombinations, max_rotation_combinations

def generate_boards(tiles: list[ThinkominoTile]) -> Iterator[ThinkominoBoard]:
	yield from BoardGenerator(tiles)

class BoardGenerator(Iterator[ThinkominoBoard]):
	def __init__(self, tiles:tuple[ThinkominoTile]):
		self.__orderer = Permutations(tiles)
		self.__rotation_combiner = None

	def __iter__(self):
		return self
	
	def __next__(self)->ThinkominoBoard:
		result = None
		while result is None:
			if self.__rotation_combiner is None:
				try:
					ordered_tiles = next(self.__orderer)
				except StopIteration:
					self.__rotation_combiner = None
					self.__orderer = None
					raise StopIteration
				self.__rotation_combiner = RotationCombinations((Rotateable(tile) for tile in ordered_tiles))
			try:
				result = next(self.__rotation_combiner)
			except StopIteration:
				self.__rotation_combiner = None
		return ThinkominoBoard(*(ThinkominoTile(*tile) for tile in result))

	def __len__(self)->int:
		return len(self.__orderer) * max_rotation_combinations(zip(self.__orderer.iterable, (1,)*len(self.__orderer.iterable)))