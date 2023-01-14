from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour
from csv import reader

def load_tiles_csv(stream) -> list[ThinkominoTile]:
	return [ThinkominoTile(*map(lambda colour: ThinkominoColour(colour), row)) for row in reader(stream)]
