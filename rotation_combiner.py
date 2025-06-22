from typing import Iterator, NamedTuple
from list_rotator import constrain_step, max_rotations, rotate

class RotationCombinations(Iterator[tuple[tuple]]):

	class Pair(NamedTuple):
		iterable:tuple
		step:int

	def __init__(self, iterable_step_pairs:tuple[Pair]):
		self.iterable_step_pairs = tuple(iterable_step_pairs)
		for pair in self.iterable_step_pairs:
			pair.iterable = tuple(pair.iterable)
			pair.step = constrain_step(pair.iterable, pair.step)
		self.__step_indices = (0,) * len(self.iterable_step_pairs)

	def __iter__(self):
		return self
	
	def __next__(self)->tuple[tuple]:
		if self.iterable_step_pairs is None:
			raise StopIteration
		result = self.__current()
		if self.__increment_rotations():
			self.iterable_step_pairs = None
		return result

	def __current(self)->tuple[tuple]:
		result = list()
		for index in range(len(self.iterable_step_pairs)):
			pair = self.iterable_step_pairs[index]
			result.append(rotate(pair.iterable, pair.step * self.__step_indices[index]))
		return tuple(result)

	def __increment_rotations(self)->bool:
		if len(self.__step_indices) < 1:
			return True
		self.__step_indices[0] += 1

		for index in range(len(self.__step_indices)):
			pair = self.iterable_step_pairs[index]
			if self.__step_indices[index] < max_rotations(pair.iterable, pair.step):
				return False #all indices in range
			self.__step_indices[index] = 0
			if index + 1 < len(self.__step_indices):
				self.__step_indices[index + 1] += 1
		return True #all indices maxed; thus last value

	def __len__(self)->int:
		product = 1
		for pair in self.iterable_step_pairs:
			product *= max_rotations(pair.iterable, pair.step)
		return product