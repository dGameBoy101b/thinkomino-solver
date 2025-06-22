from unittest import TestCase
from list_rotator import rotate_list

class ListRotatorTests(TestCase):
	
	def test_empty(self):
		rotator = rotate_list([])
		self.assertEqual(len(rotator), 1)
		self.assertSequenceEqual(next(rotator), [])
		with self.assertRaises(StopIteration):
			next(rotator)
	
	def test_1(self):
		rotator = rotate_list([1])
		self.assertEqual(len(rotator), 1)
		self.assertSequenceEqual(next(rotator), [1])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_2(self):
		rotator = rotate_list(['a',3.4])
		self.assertEqual(len(rotator), 2)
		self.assertSequenceEqual(next(rotator), ['a',3.4])
		self.assertSequenceEqual(next(rotator), [3.4,'a'])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3(self):
		rotator = rotate_list([['a',1],3.4,'string'])
		self.assertEqual(len(rotator), 3)
		self.assertSequenceEqual(next(rotator),[['a',1],3.4,'string'])
		self.assertSequenceEqual(next(rotator), ['string',['a',1],3.4])
		self.assertSequenceEqual(next(rotator), [3.4,'string',['a',1]])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_step_type_error(self):
		with self.assertRaises(TypeError):
			next(rotate_list([1,2,3],'string'))

	def test_step_value_error(self):
		with self.assertRaises(ValueError):
			next(rotate_list([1,2,3], 0))
		with self.assertRaises(ValueError):
			next(rotate_list([1,2,3], -1))
		with self.assertRaises(ValueError):
			next(rotate_list([1,2,3], 4))

	def test_5_step_2(self):
		rotator = rotate_list([1,2,3,4,5], 2)
		self.assertEqual(len(rotator), 5)
		self.assertSequenceEqual(next(rotator), [1,2,3,4,5])
		self.assertSequenceEqual(next(rotator), [4,5,1,2,3])
		self.assertSequenceEqual(next(rotator), [2,3,4,5,1])
		self.assertSequenceEqual(next(rotator), [5,1,2,3,4])
		self.assertSequenceEqual(next(rotator), [3,4,5,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_4_step_2(self):
		rotator = rotate_list([1,2,3,4], 2)
		self.assertEqual(len(rotator), 2)
		self.assertSequenceEqual(next(rotator), [1,2,3,4])
		self.assertSequenceEqual(next(rotator), [3,4,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)
