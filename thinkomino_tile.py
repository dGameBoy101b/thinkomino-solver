from thinkomino_colour import ThinkominoColour

class ThinkominoTile(tuple):

	def __init__(self, colours: list[ThinkominoColour]):
		if len(colours) != 6:
			raise IndexError('colours must contain exactly 6 items')
		seen_colours = set()
		for item in colours:
			if not isinstance(item, ThinkominoColour):
				raise ValueError('every item in colours must be a ThinkominoColour')
			if item in seen_colours:
				raise ValueError('every item in colours must be unique')
			seen_colours |= {item}
		self = tuple(colours)
