from thinkomino_tile import ThinkominoTile
from thinkomino_colour import ThinkominoColour
from thinkomino_board import ThinkominoBoard
from logging import Logger
from csv import reader
from list_permuter import permute_list
from list_rotator import rotate_list
from multiprocessing.pool import Pool

class ThinkominoSolver:
	def __init__(self, logger: Logger = None):
		if logger is not None and not isinstance(logger, Logger):
			raise TypeError('logger must be a Logger or None')
		self.logger = logger

	def load_tiles_csv(self, path: str) -> list[ThinkominoTile]:
		#log start
		if self.logger is not None:
			self.logger.info(f'Loading tiles from {path!r}...')
		try:
			#load tiles from csv
			file = open(path)
			tiles = [ThinkominoTile(map(lambda colour: ThinkominoColour(colour), row)) for row in reader(file)]
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
			for order in permute_list(tiles):
				def permute_rotations(tiles: list[ThinkominoTile]) -> list[ThinkominoTile]:
					for rotation in rotate_list(tiles[0]):
						yield [ThinkominoTile(rotation)] + permute_rotations(tiles[0:])
				for state in permute_rotations(order):
					board = ThinkominoBoard(*state)
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

	async def solve_board(self, board: ThinkominoBoard)->bool:
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
					solvers[board] = pool.apply_async(self.solve_board(board))
				#check solver processes
				for key in solvers:
					if solvers[key].ready():
						if solvers[key].get():
							#log successful solution
							if self.logger is not None:
								self.logger.debug(f'Solution found: {key!r}')
								self.logger.info(f'Solution found: {hash(key)}')
							return key
						del solvers[key]
		#log failed solution
		if self.logger is not None:
			self.logger.info('No solution found')

if __name__ == '__main__':
	#parse command line arguments
	from argparse import ArgumentParser
	from logging.config import dictConfig
	TILES_CSV_ARG_NAME = 'tiles_csv'
	SOLVER_PROCESSES_ARG_NAME = 'solver_processes'
	LOGGER_XML_FILE_ARG_NAME = 'logger_config_file'
	parser = ArgumentParser(description='Solve a Thinkomino puzzle')
	parser.add_argument(TILES_CSV_ARG_NAME, required=True)
	parser.add_argument(SOLVER_PROCESSES_ARG_NAME, type=int, default=1)
	parser.add_argument(LOGGER_XML_FILE_ARG_NAME, type=lambda file: dictConfig(file), required=False)
	args = parser.parse_args()
	#run solver
	solver = ThinkominoSolver(args[LOGGER_XML_FILE_ARG_NAME])
	solution = solver.main(tiles_csv=args[TILES_CSV_ARG_NAME], solver_processes=args[SOLVER_PROCESSES_ARG_NAME])
	#display solution
	if solution is not None:
		pass #todo