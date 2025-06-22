from typing import Iterable, Iterator
from math import copysign

def rotate(iterable:tuple, step:int)->tuple:
	iterable = tuple(iterable)
	if len(iterable) < 2:
		return iterable
	index = -int(copysign(abs(step) % len(iterable), step))
	return iterable[index:] + iterable[:index]

class Rotations(Iterator[Iterable]):
	def __init__(self, iterable:Iterable, step:int=1):
		self.iterable = tuple(iterable)
		self.__step_index = 0
		self.__len = None
		try:
			step = int(step)
		except ValueError as x:
			raise TypeError('step must be an integer', x)
		self.step = 1 if len(self.iterable) < 1 else int(copysign(abs(step) % len(self.iterable), step))

	def __len__(self) -> int:
		if len(self.iterable) < 1 or self.step == 0:
			return 1
		if self.__len is None:
			loops = 1
			while len(self.iterable) * loops % abs(self.step) > 0:
				loops += 1
			self.__len = len(self.iterable) * loops // abs(self.step)
		return self.__len

	def __iter__(self):
		return self
	
	def __next__(self) -> tuple:
		if (self.__step_index >= len(self)):
			raise StopIteration
		result = rotate(self.iterable, self.__step_index * self.step)
		self.__step_index += 1
		return result
