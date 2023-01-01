from thinkomino_colour import ThinkominoColour

class ThinkominoTile(tuple):

	def __init__(self, iterable):
		if len(iterable) != 6:
			raise IndexError('iterable must contain exactly 6 items')
		colours = set()
		for item in iterable:
			if not isinstance(item, ThinkominoColour):
				raise ValueError('every item in iterable must be a ThinkominoColour')
			if item in colours:
				raise ValueError('every item in iterable must be unique')
			colours |= {item}
		self = tuple(iterable)