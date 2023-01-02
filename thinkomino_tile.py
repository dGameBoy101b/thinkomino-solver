from thinkomino_colour import ThinkominoColour

class ThinkominoTile:

	def __init__(self, *colours: tuple[ThinkominoColour]):
		if len(colours) != 6:
			raise IndexError('colours must contain exactly 6 items')
		seen_colours = set()
		for item in colours:
			if not isinstance(item, ThinkominoColour):
				raise ValueError('every item in colours must be a ThinkominoColour')
			if item in seen_colours:
				raise ValueError('every item in colours must be unique')
			seen_colours |= {item}
		self.__sides = tuple(colours)

	def __repr__(self)->str:
		return f'ThinkominoTile({", ".join(map(repr, self.__sides))!s})'

	def __len__(self)->int:
		return 6

	def __iter__(self)->iter:
		return iter(self.__sides)

	def __getitem__(self, key)->ThinkominoColour:
		if isinstance(key, str):
			if key == 'east' or key == 'e':
				return self[0]
			if key == 'north east' or key == 'ne':
				return self[1]
			if key == 'north west' or key == 'nw':
				return self[2]
			if key == 'west' or key == 'w':
				return self[3]
			if key == 'south west' or key == 'sw':
				return self[4]
			if key == 'south east' or key == 'se':
				return self[5]
			raise KeyError
		return self.__sides[key]

	def __contains__(self, item)->bool:
		return isinstance(item, ThinkominoColour)

	def __getattr__(self, name: str)->ThinkominoColour:
		if name == 'east' or name == 'e':
			return self[0]
		if name == 'north_east' or name == 'ne':
			return self[1]
		if name == 'north_west' or name == 'nw':
			return self[2]
		if name == 'west' or name == 'w':
			return self[3]
		if name == 'south_west' or name == 'sw':
			return self[4]
		if name == 'south_east' or name == 'se':
			return self[5]
		raise AttributeError

	def __eq__(self, other)->bool:
		return isinstance(other, ThinkominoTile) and self.__sides == other.__sides
