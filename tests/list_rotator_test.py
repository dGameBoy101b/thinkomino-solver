from unittest import TestCase
from list_rotator import rotate_list

class ListRotatorTests(TestCase):
	
	def test_empty(self):
		with self.assertRaises(StopIteration):
			next(rotate_list([]))
	
	def test_one(self):
		rotator = rotate_list([1])
		self.assertEqual(next(rotator), [1])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_two(self):
		rotator = rotate_list(['a',3.4])
		self.assertEqual(next(rotator), ['a',3.4])
		self.assertEqual(next(rotator), [3.4,'a'])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_three(self):
		rotator = rotate_list([['a',1],3.4,'string'])
		self.assertEqual(next(rotator),[['a',1],3.4,'string'])
		self.assertEqual(next(rotator), ['string',['a',1],3.4])
		self.assertEqual(next(rotator), [3.4,'string',['a',1]])
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

	def test_step(self):
		rotator = rotate_list([1,2,3,4,5], 2)
		self.assertEqual(next(rotator), [1,2,3,4,5])
		self.assertEqual(next(rotator), [4,5,1,2,3])
		self.assertEqual(next(rotator), [2,3,4,5,1])
		self.assertEqual(next(rotator), [5,1,2,3,4])
		self.assertEqual(next(rotator), [3,4,5,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_iteration_type_error(self):
		with self.assertRaises(TypeError):
			next(rotate_list([1,2,3], 1, 'string'))

	def test_iteration_value_error(self):
		with self.assertRaises(ValueError):
			next(rotate_list([1,2,3], 1, -1))

	def test_iteration_zero(self):
		with self.assertRaises(StopIteration):
			next(rotate_list([1,2,3], 1, 0))

	def test_iteration_excess(self):
		rotator = rotate_list([1,2,3], 1, 4)
		self.assertEqual(next(rotator), [1,2,3])
		self.assertEqual(next(rotator), [3,1,2])
		self.assertEqual(next(rotator), [2,3,1])
		self.assertEqual(next(rotator), [1,2,3])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_iteration_trim(self):
		rotator = rotate_list([1,2,3], 1, 2)
		self.assertEqual(next(rotator), [1,2,3])
		self.assertEqual(next(rotator), [3,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)
