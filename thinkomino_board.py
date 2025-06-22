from thinkomino_tile import ThinkominoTile

class ThinkominoBoard:


	def __init__(self, north: ThinkominoTile = None, north_west: ThinkominoTile = None, south_west: ThinkominoTile = None, south: ThinkominoTile = None, south_east: ThinkominoTile = None, north_east: ThinkominoTile = None):
		for tile in (north, north_west, south_west, south, south_east, north_east):
			if (tile is not None) and (not isinstance(tile, ThinkominoTile)):
				raise ValueError('ThinkominoBoard may only contain ThinkominoTiles')
		self.north = north
		self.north_west = north_west
		self.south_west = south_west
		self.south = south
		self.south_east = south_east
		self.north_east = north_east

	ADJACENCIES = frozenset({
		(('n','sw'), ('nw','ne')),
		(('n','se'), ('ne','nw')),
		(('nw','e'), ('ne','w')),
		(('nw','sw'), ('sw','ne')),
		(('nw','w'), ('s','e')),
		(('ne','sw'), ('s','ne')),
		(('ne','se'), ('se','nw')),
		(('sw','e'), ('s','w')),
		(('s','e'), ('se','w'))})

	def is_solved(self)->bool:
		for tile in self:
			if tile is None:
				return False
		for adjacency in ThinkominoBoard.ADJACENCIES:
			if self[adjacency[0][0]][adjacency[0][1]] != self[adjacency[1][0]][adjacency[1][1]]:
				return False
		return True

	def __repr__(self)->str:
		return f'ThinkominoBoard({self.north!r}, {self.north_west!r}, {self.south_west!r}, {self.south!r}, {self.south_east!r}, {self.north_east!r})'

	def __eq__(self, other)->bool:
		return isinstance(other, ThinkominoBoard) and self.north == other.north and self.north_west == other.north_west and self.south_west == other.south_west and self.north_west == other.north_west

	def __hash__(self)->int:
		return hash((self.north, self.north_west, self.south_west, self.south, self.south_east, self.north_east))

	def __getattr__(self, name:str)->ThinkominoTile:
		if name == 'n':
			return self.north
		if name == 'nw':
			return self.north_west
		if name == 'sw':
			return self.south_west
		if name == 's':
			return self.south
		if name == 'se':
			return self.south_east
		if name == 'ne':
			return self.north_east
		raise AttributeError

	def __iter__(self)->iter:
		return iter((self.north, self.north_west, self.south_west, self.south, self.south_east, self.north_east))

	def __getitem__(self, key)->ThinkominoTile:
		if isinstance(key, str):
			if key == 'north' or key == 'n':
				return self.north
			if key == 'north west' or key == 'nw':
				return self.north_west
			if key == 'south west' or key == 'sw':
				return self.south_west
			if key == 'south' or key == 's':
				return self.south
			if key == 'south east' or key == 'se':
				return self.south_east
			if key == 'north east' or key == 'ne':
				return self.north_east
			raise KeyError
		return (self.north, self.north_west, self.south_west, self.south, self.south_east, self.north_east)[key]
