from typing import Generator
from thinkomino_tile import ThinkominoTile
from thinkomino_board import ThinkominoBoard
from multiprocessing.pool import Pool
from logging import getLogger
from thinkomino_board_generator import generate_boards
from thinkomino_tiles_csv_loader import load_tiles_csv

class ThinkominoSolver:
	def __init__(self):
		self.logger = getLogger(__name__)

	def _load_tiles_csv(self, path: str) -> list[ThinkominoTile]:
		#log start
		if self.logger is not None:
			self.logger.info(f'Loading tiles from {path!r}...')
		try:
			#load tiles from csv
			tiles = None
			with open(path, 'rt') as file:
				tiles = load_tiles_csv(file)
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

	def _generate_boards(self, tiles: list[ThinkominoTile]) -> Generator[ThinkominoBoard]:
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

	def _solve_board(self, board: ThinkominoBoard)->bool:
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

	def __call__(self, tiles_csv: str = None, tiles: list[ThinkominoTile] = None, solver_processes: int = 1) -> ThinkominoBoard:
		#load tiles
		if tiles_csv is not None:
			tiles = self._load_tiles_csv(tiles_csv)
		#solve
		solvers = dict()
		with Pool(solver_processes) as pool:
			generator = self._generate_boards(tiles)
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
					solvers[board] = pool.apply_async(self._solve_board, [board])
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

