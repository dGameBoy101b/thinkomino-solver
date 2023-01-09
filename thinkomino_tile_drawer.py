from turtle import RawTurtle, Vec2D
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour

class ThinkominoTileDrawer:

	def __init__(self, red = 'red', orange = 'orange', yellow = 'yellow', green = 'green', blue = 'blue', purple = 'purple', outline = 'black', outline_width: int = 1):
		self.red = red
		self.orange = orange
		self.yellow = yellow
		self.green = green
		self.blue = blue
		self.purple = purple
		self.outline = outline
		outline_width = int(outline_width)
		if outline_width < 0:
			raise ValueError('outline_width must be 0 or greater')
		self.outline_width = outline_width

	def draw(self, tile: ThinkominoTile, turtle: RawTurtle, radius: float, center: Vec2D = Vec2D(0,0), rotation: float = 0):
		COLOUR_MAP = {
			ThinkominoColour.RED: self.red,
			ThinkominoColour.ORANGE: self.orange,
			ThinkominoColour.YELLOW: self.yellow,
			ThinkominoColour.GREEN: self.green,
			ThinkominoColour.BLUE: self.blue,
			ThinkominoColour.PURPLE: self.purple}
		turtle.pencolor(self.outline)
		turtle.pensize(self.outline_width)
		turtle.penup()
		turtle.setposition(center)
		turtle.setheading(rotation)
		turtle.pendown()
		for colour in tile:
			turtle.fillcolor(COLOUR_MAP[colour])
			turtle.begin_fill()
			turtle.forward(radius)
			turtle.setheading(turtle.heading() + 120)
			turtle.forward(radius)
			turtle.setheading(turtle.heading() + 120)
			turtle.forward(radius)
			turtle.end_fill()
			turtle.setheading(turtle.heading() + 180)

if __name__ == '__main__':
	from turtle import Screen
	screen = Screen()
	screen.delay(0)
	turtle = RawTurtle(screen, visible=False)
	turtle.speed(0)
	TILE = ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
	drawer = ThinkominoTileDrawer()
	drawer.draw(TILE, turtle, 100, rotation=-30)