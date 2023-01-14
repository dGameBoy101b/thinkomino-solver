from thinkomino_tile import ThinkominoTile
from thinkomino_board import ThinkominoBoard
from multiprocessing.pool import Pool
from logging import getLogger
from thinkomino_board_generator import generate_boards
from thinkomino_tiles_csv_loader import load_tiles_csv

class ThinkominoSolver:
	def __init__(self):
		self.logger = getLogger(__name__)

	def load_tiles_csv(self, path: str) -> list[ThinkominoTile]:
		#log start
		if self.logger is not None:
			self.logger.info(f'Loading tiles from {path!r}...')
		try:
			#load tiles from csv
			tiles = load_tiles_csv(path)
			#log end
			if self.logger is not None:
				self.logger.debug(f'Loaded tiles: {tiles!r}')
				self.logger.info(f'Finished loading tiles from {path!r}')
			return tiles
		except Exception as x:
			#log error
			if self.logger is not None:
				self.logger.error(f'Failed to load tiles: {x!r}')
			raise x

	def generate_boards(self, tiles: list[ThinkominoTile]) -> ThinkominoBoard:
		#log start
		if self.logger is not None:
			self.logger.info('Generating boards...')
		try:
			#generate board
			for board in generate_boards(tiles):
				#log generated board
				if self.logger is not None:
					self.logger.debug(f'Generated board: {board!r}')
				yield board
			#log end
			if self.logger is not None:
				self.logger.info('Finished generating boards')
		except Exception as x:
			#log error
			if self.logger is not None:
				self.logger.error(f'Failed to generate boards: {x!r}')
			raise x

	def solve_board(self, board: ThinkominoBoard)->bool:
		id = hash(board)
		#log start
		if self.logger is not None:
			self.logger.info(f'Solving board: {id}...')
			self.logger.debug(f'Solving board: {id} = {board!r}')
		try:
			#solve
			result = board.is_solved()
			#log end
			if self.logger is not None:
				self.logger.debug(f'Is board {id} solved: {result}')
				self.logger.info(f'Finished solving board: {id}')
			return result
		except Exception as x:
			if self.logger is not None:
				self.logger.error(f'Failed to solve board {id}')
			raise x

	def main(self, tiles_csv: str = None, tiles: list[ThinkominoTile] = None, solver_processes: int = 1) -> ThinkominoBoard:
		#load tiles
		if tiles_csv is not None:
			tiles = self.load_tiles_csv(tiles_csv)
		#solve
		solvers = dict()
		with Pool(solver_processes) as pool:
			generator = self.generate_boards(tiles)
			board = None
			while generator is not None or len(solvers) > 0:
				#generate next board
				if generator is not None:
					try:
						board = next(generator)
					except StopIteration:
						generator = None
						board = None
				#start solver process
				if board is not None:
					solvers[board] = pool.apply_async(self.solve_board, [board])
				#check solver processes
				to_delete = set()
				for key in solvers:
					if solvers[key].ready():
						if solvers[key].get():
							#log successful solution
							if self.logger is not None:
								self.logger.debug(f'Solution found: {key!r}')
								self.logger.info(f'Solution found: {hash(key)}')
							return key
						to_delete.add(key)
				#delete failed solutions
				for key in to_delete:
					#log failed solution
					if self.logger is not None:
						self.logger.debug(f'Solution discarded: {key!r}')
						self.logger.info(f'Solution discarded: {hash(key)}')
					del solvers[key]
		#log failed solution
		if self.logger is not None:
			self.logger.info('No solution found')

if __name__ == '__main__':
	from argparse import ArgumentParser
	from turtle import Screen, RawTurtle
	from thinkomino_board_drawer import draw_board
	from logging.config import dictConfig
	from json import load
	from sys import stdin, stdout, stderr
	#parse command line arguments
	TILES_CSV_ARG_NAME = 'tiles_csv'
	SOLVER_PROCESSES_ARG_NAME = 'solver_processes'
	LOGGER_JSON_FILE_ARG_NAME = 'logger_config_file'
	SNAPSHOT_FOLDER_ARG_NAME = 'snapshot_folder'
	parser = ArgumentParser(description='Solve a Thinkomino puzzle')
	parser.add_argument(TILES_CSV_ARG_NAME, type=str, help='Path to the csv file storing the available tiles')
	parser.add_argument(SOLVER_PROCESSES_ARG_NAME, type=int, default=1, help='The maximum number of processes that can be used to solve generated boards')
	parser.add_argument(LOGGER_JSON_FILE_ARG_NAME, type=str, default=None, help='Path to the json file used to configure a logger')
	parser.add_argument(SNAPSHOT_FOLDER_ARG_NAME, type=str, default=None, help='Path to the folder used to export solution snapshots to')
	args = vars(parser.parse_args())
	#config logger
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
	if args[LOGGER_JSON_FILE_ARG_NAME] is not None:
		with open(args[LOGGER_JSON_FILE_ARG_NAME], 'rt') as file:
			dictConfig(load(file, object_hook=cast_std_streams))
	#run solver
	solver = ThinkominoSolver()
	solution = solver.main(tiles_csv=args[TILES_CSV_ARG_NAME], solver_processes=args[SOLVER_PROCESSES_ARG_NAME])
	#display solution
	screen = Screen()
	screen.delay(0)
	if solution is not None:
		turtle = RawTurtle(screen, visible=False)
		turtle.speed(0)
		draw_board(solution, turtle)
	screen.exitonclick()
