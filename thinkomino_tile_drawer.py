from turtle import RawTurtle
from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour

def draw_tile(tile: ThinkominoTile, turtle: RawTurtle, radius: float, red = 'red', orange = 'orange', yellow = 'yellow', green = 'green', blue = 'blue', purple = 'purple'):
	COLOUR_MAP = {
		ThinkominoColour.RED: red,
		ThinkominoColour.ORANGE: orange,
		ThinkominoColour.YELLOW: yellow,
		ThinkominoColour.GREEN: green,
		ThinkominoColour.BLUE: blue,
		ThinkominoColour.PURPLE: purple}
	turtle.setheading(turtle.heading() - 30)
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
	turtle = RawTurtle(screen)
	turtle.speed(0)
	TILE = ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
	draw_tile(TILE, turtle, 100)
