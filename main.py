from argparse import ArgumentParser
from thinkomino_solver import ThinkominoSolver
from turtle import Screen, RawTurtle
from thinkomino_board_drawer import draw_board
from logging.config import dictConfig
from json import load
from sys import stdin, stdout, stderr

TILES_CSV_ARG_NAME = 'tiles_csv'
SOLVER_PROCESSES_ARG_NAME = 'solver_processes'
LOGGER_JSON_FILE_ARG_NAME = 'logger_config_file'
DEFAULT_LOG_CONFIG_PATH = 'logger.json'
SNAPSHOT_FOLDER_ARG_NAME = 'snapshot_folder'

def arg_parser() -> ArgumentParser:
	parser = ArgumentParser(description='Solve a Thinkomino puzzle')
	parser.add_argument(TILES_CSV_ARG_NAME, type=str, help='Path to the csv file storing the available tiles')
	parser.add_argument(SOLVER_PROCESSES_ARG_NAME, nargs='?', type=int, default=None, help='The maximum number of processes that can be used to solve generated boards')
	parser.add_argument(LOGGER_JSON_FILE_ARG_NAME, nargs='?', type=str, default=DEFAULT_LOG_CONFIG_PATH, help='Path to the json file used to configure a logger')
	parser.add_argument(SNAPSHOT_FOLDER_ARG_NAME, nargs='?', type=str, default=None, help='Path to the folder used to export solution snapshots to')
	return parser

def cast_std_streams(json_data: dict) -> dict:
	CLASS_KEY = 'class'
	STREAM_KEY = 'stream'
	STREAM_CAST_MAP = {
		'sys.stdin': stdin,
		'sys.stdout': stdout,
		'sys.stderr': stderr}
	if CLASS_KEY in json_data and json_data[CLASS_KEY] == 'logging.StreamHandler' and STREAM_KEY in json_data and json_data[STREAM_KEY] in STREAM_CAST_MAP:
		json_data[STREAM_KEY] = STREAM_CAST_MAP[json_data[STREAM_KEY]]
	return json_data

def main():
	#parse command line arguments
	parser = arg_parser()
	args = parser.parse_args().__dict__
	#config logger
	if args[LOGGER_JSON_FILE_ARG_NAME] is not None:
		with open(args[LOGGER_JSON_FILE_ARG_NAME], 'rt') as file:
			dictConfig(load(file, object_hook=cast_std_streams))
	#run solver
	solver = ThinkominoSolver()
	solution = solver(tiles_csv=args[TILES_CSV_ARG_NAME], solver_processes=args[SOLVER_PROCESSES_ARG_NAME])
	#display solution
	screen = Screen()
	screen.delay(0)
	if solution is not None:
		turtle = RawTurtle(screen, visible=False)
		turtle.speed(0)
		draw_board(solution, turtle)
	screen.exitonclick()

if __name__ == '__main__':
	main()