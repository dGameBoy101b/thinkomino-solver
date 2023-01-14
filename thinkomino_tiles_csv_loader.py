from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour
from csv import reader

def load_tiles_csv(path: str) -> list[ThinkominoTile]:
	with open(path) as file:
		return [ThinkominoTile(*map(lambda colour: ThinkominoColour(colour), row)) for row in reader(file)]
