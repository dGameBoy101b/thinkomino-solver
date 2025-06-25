from dataclasses import dataclass
from typing import Iterator
from list_rotator import constrain_step, max_rotations, rotate

class RotationCombinations(Iterator[tuple[tuple]]):

	@dataclass(init=False, frozen=True)
	class Rotateable:
		iterable: tuple
		step: int = 1

		def __init__(self, iterable:tuple, step:int = 1):
			super().__setattr__("iterable", tuple(iterable))
			super().__setattr__("step", constrain_step(iterable, step))

		def __iter__(self):
			return iter((self.iterable, self.step))

	def __init__(self, rotateables:tuple[Rotateable]):
		self.rotateables = tuple(RotationCombinations.Rotateable(*rotateable) for rotateable in rotateables)
		self.__step_indices = [0] * len(self.rotateables)

	def __iter__(self):
		return self
	
	def __next__(self)->tuple[tuple]:
		if self.rotateables is None:
			raise StopIteration
		result = self.__current()
		if self.__increment_rotations():
			self.rotateables = None
		return result

	def __current(self)->tuple[tuple]:
		result = list()
		for index in range(len(self.rotateables)):
			rotableable = self.rotateables[index]
			result.append(rotate(rotableable.iterable, rotableable.step * self.__step_indices[index]))
		return tuple(result)

	def __increment_rotations(self)->bool:
		if len(self.__step_indices) < 1:
			return True
		self.__step_indices[0] += 1

		for index in range(len(self.__step_indices)):
			rotateable = self.rotateables[index]
			if self.__step_indices[index] < max_rotations(rotateable.iterable, rotateable.step):
				return False #all indices in range
			self.__step_indices[index] = 0
			if index + 1 < len(self.__step_indices):
				self.__step_indices[index + 1] += 1
		return True #all indices maxed; thus last value

	def __len__(self)->int:
		product = 1
		for rotateable in self.rotateables:
			product *= max_rotations(rotateable.iterable, rotateable.step)
		return product