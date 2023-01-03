from thinkomino_colour import ThinkominoColour

class ThinkominoTile:

	def __init__(self, east: ThinkominoColour, north_east: ThinkominoColour, north_west: ThinkominoColour,
		west: ThinkominoColour, south_west: ThinkominoColour, south_east: ThinkominoColour):
		seen_colours = set()
		for colour in (east, north_east, north_west, west, south_west, south_east):
			if not isinstance(colour, ThinkominoColour):
				raise ValueError('ThinkominoTile may only contain ThinkominoColours')
			if colour in seen_colours:
				raise ValueError('ThinkominoTile may only contain unique ThinkominoColours')
			seen_colours |= {colour}
		self.east = east
		self.north_east = north_east
		self.north_west = north_west
		self.west = west
		self.south_west = south_west
		self.south_east = south_east

	def __repr__(self)->str:
		return f'ThinkominoTile({self.east!r}, {self.north_east!r}, {self.north_west!r}, {self.west!r}, {self.south_west!r}, {self.south_east!r})'

	def __eq__(self, other)->bool:
		return isinstance(other, ThinkominoTile) and self.east == other.east and self.north_east == other.north_east and self.north_west == other.north_west and self.west == other.west and self.south_west == other.south_west and self.south_east == other.south_east

	def __hash__(self)->int:
		return hash((self.east, self.north_east, self.north_west, self.west, self.south_west, self.south_east))

	def __getattr__(self, name: str)->ThinkominoColour:
		if name == 'e':
			return self.east
		if name == 'ne':
			return self.north_east
		if name == 'nw':
			return self.north_west
		if name == 'w':
			return self.west
		if name == 'sw':
			return self.south_west
		if name == 'se':
			return self.south_east
		raise AttributeError

	def __len__(self)->int:
		return 6

	def __iter__(self)->iter:
		return iter((self.east, self.north_east, self.north_west, self.west, self.south_west, self.south_east))

	def __contains__(self, item)->bool:
		return isinstance(item, ThinkominoColour)

	def __getitem__(self, key)->ThinkominoColour:
		if isinstance(key, str):
			if key == 'east' or key == 'e':
				return self.east
			if key == 'north east' or key == 'ne':
				return self.north_east
			if key == 'north west' or key == 'nw':
				return self.north_west
			if key == 'west' or key == 'w':
				return self.west
			if key == 'south west' or key == 'sw':
				return self.south_west
			if key == 'south east' or key == 'se':
				return self.south_east
			raise KeyError
		return (self.east, self.north_east, self.north_west, self.west, self.south_west, self.south_east)[key]
