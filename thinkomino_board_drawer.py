from turtle import RawTurtle
from thinkomino_board import ThinkominoBoard
from thinkomino_tile_drawer import draw_tile

def draw_board(board: ThinkominoBoard, turtle: RawTurtle, radius: float, red = 'red', orange = 'orange', yellow = 'yellow', green = 'green', blue = 'blue', purple = 'purple', inner_colour = 'black', inner_width: int = 1, outer_colour = 'grey', outer_width: int = 5):
	TILE_HEADING = turtle.heading()
	turtle.setheading(turtle.heading() + 90)
	coefficent = .5
	turtle.penup()
	for tile in board:
		heading = turtle.heading()
		turtle.forward((1.5 + coefficent) * radius)
		turtle.setheading(TILE_HEADING)
		draw_tile(tile, turtle, radius, red, orange, yellow, green, blue, purple, inner_colour, inner_width, outer_colour, outer_width)
		turtle.penup()
		turtle.setheading(heading)
		turtle.backward((1.5 + coefficent) * radius)
		turtle.setheading(turtle.heading() + 60)
		coefficent *= -1

if __name__ == '__main__':
	from turtle import RawTurtle, Screen
	from thinkomino_tile import ThinkominoTile
	from thinkomino_colour import ThinkominoColour
	screen = Screen()
	screen.delay(0)
	turtle = RawTurtle(screen)
	turtle.speed(0)
	TILE = ThinkominoTile(ThinkominoColour.RED, ThinkominoColour.ORANGE, ThinkominoColour.YELLOW, ThinkominoColour.GREEN, ThinkominoColour.BLUE, ThinkominoColour.PURPLE)
	BOARD = ThinkominoBoard(TILE,TILE,TILE,TILE,TILE,TILE)
	draw_board(BOARD, turtle, 100)
	pass