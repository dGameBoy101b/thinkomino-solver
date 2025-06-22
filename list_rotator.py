from typing import Iterable, Iterator
from math import copysign

def constrain_step(iterable:tuple, step:int)->int:
	return 0 if len(iterable) < 1 else int(copysign(abs(step) % len(iterable), step))

def rotate(iterable:tuple, step:int)->tuple:
	iterable = tuple(iterable)
	if len(iterable) < 2:
		return iterable
	index = -constrain_step(iterable, step)
	return iterable[index:] + iterable[:index]

def max_rotations(iterable:tuple, step:int)->int:
	iterable_len = len(iterable)
	if iterable_len < 1:
		return 1
	step = constrain_step(iterable, step)
	if step == 0:
		return 1
	abs_step = abs(step)
	loops = 1
	while iterable_len * loops % abs_step > 0:
		loops += 1
	return iterable_len * loops // abs_step

class Rotations(Iterator[Iterable]):
	def __init__(self, iterable:Iterable, step:int=1):
		self.iterable = tuple(iterable)
		self.__step_index = 0
		self.__len = None
		try:
			step = int(step)
		except ValueError as x:
			raise TypeError('step must be an integer', x)
		self.step = constrain_step(self.iterable, step)

	def __len__(self) -> int:
		if self.__len is None:
			self.__len = max_rotations(self.iterable, self.step)
		return self.__len

	def __iter__(self):
		return self
	
	def __next__(self) -> tuple:
		if (self.__step_index >= len(self)):
			raise StopIteration
		result = rotate(self.iterable, self.__step_index * self.step)
		self.__step_index += 1
		return result
