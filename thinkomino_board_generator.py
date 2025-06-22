from thinkomino_board import ThinkominoBoard
from thinkomino_tile import ThinkominoTile
from list_permuter import permute_list
from list_rotator import Rotations

def generate_boards(tiles: list[ThinkominoTile]) -> ThinkominoBoard:
	for order in permute_list(tiles):
		def permute_rotations(tiles: list[ThinkominoTile]) -> list[ThinkominoTile]:
			if len(tiles) < 2:
				yield tiles
				return
			for rotation in Rotations(tiles[0]):
				for permutation in permute_rotations(tiles[1:]):
					yield [ThinkominoTile(*rotation)] + permutation
		for state in permute_rotations(order):
			yield ThinkominoBoard(*state)
