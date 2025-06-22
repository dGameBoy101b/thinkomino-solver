from typing import Iterable, Iterator

def rotate_list(ls:list, step:int=1)->Iterator[tuple]:
	return Rotations(ls, step)

class Rotations(Iterator[Iterable]):
	def __init__(self, iterable:Iterable, step:int=1):
		self.iterable = tuple(iterable)
		self.__step_index = 0
		self.__len = None
		try:
			step = int(step)
		except ValueError as x:
			raise TypeError('step must be an integer', x)
		if step < 1:
			raise ValueError('step must be 1 or greater')
		if len(self.iterable) > 0 and step > len(self.iterable):
			raise ValueError(f'step must be lesser than or equal to the length of the iterable ({len(self.iterable)})')
		self.step = step

	def __len__(self) -> int:
		if len(self.iterable) < 1:
			return 1
		if self.__len is None:
			loops = 1
			while len(self.iterable) * loops % self.step > 0:
				loops += 1
			self.__len = len(self.iterable) * loops // self.step
		return self.__len

	def __iter__(self):
		return self
	
	def __next__(self) -> tuple:
		if (self.__step_index >= len(self)):
			raise StopIteration
		if len(self.iterable) < 1:
			self.__step_index += 1
			return tuple()
		index = -self.__step_index * self.step % len(self.iterable)
		self.__step_index += 1
		return self.iterable[index:] + self.iterable[:index]
