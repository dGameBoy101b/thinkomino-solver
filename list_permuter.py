from typing import Iterator
from math import factorial

'''Obsolete: Use Permutations iterator class instead.'''
def permute_list(ls:list)->Iterator[tuple]:
	return Permutations(ls)

class Permutations(Iterator[tuple]):
	def __init__(self, iterable:tuple):
		self.iterable = tuple(iterable)
		self.__subpermuter = None if len(self.iterable) < 1 else Permutations(self.iterable[1:])
		self.__subpermutation = None
		self.__index = 0

	def __len__(self)->int:
		return factorial(len(self.iterable))

	def __iter__(self):
		return self
	
	def __next__(self)->tuple:
		if self.__subpermuter is None:
			if self.__index > 0:
				raise StopIteration
			self.__index = 1
			return tuple()
		
		if self.__index >= len(self.iterable):
			self.__subpermutation = None

		if self.__subpermutation is None:
			try:
				self.__subpermutation = next(self.__subpermuter)
			except StopIteration:
				self.__subpermuter = None
				raise StopIteration
			self.__index = 0

		permutation = self.__subpermutation[:self.__index] + (self.iterable[0],) + self.__subpermutation[self.__index:]
		self.__index += 1
		return permutation