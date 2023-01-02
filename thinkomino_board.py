from thinkomino_tile import ThinkominoTile

class ThinkominoBoard(tuple):

	ADJACENCIES = frozenset({
		((0,4), (1,1)),
		((0,5), (2,2)),
		((1,0), (2,3)),
		((1,4), (3,1)),
		((1,5), (4,2)),
		((2,4), (4,1)),
		((2,5), (5,2)),
		((3,0), (4,3)),
		((4,0), (5,3))})

	def __init__(self, tiles: list[ThinkominoTile]):
		if len(tiles) != 6:
			raise IndexError('Thinkomino board must have exactly 6 tiles')
		for tile in tiles:
			if tile is not None and not isinstance(tile, ThinkominoTile):
				raise ValueError('Thinkomino board may only contain thinkomino tiles')
		self = tuple(tiles)

	def is_solved(self)->bool:
		for tile in self:
			if tile is None:
				return False
		for adjacency in ThinkominoBoard.ADJACENCIES:
			if self[adjacency[0][0]][adjacency[0][1]] != self[adjacency[1][0]][adjacency[1][1]]:
				return False
		return True
