from unittest import TestCase
from list_rotator import Rotations

class ListRotatorTests(TestCase):
	
	def test_empty(self):
		rotator = Rotations([])
		self.assertEqual(len(rotator), 1)
		self.assertSequenceEqual(next(rotator), [])
		with self.assertRaises(StopIteration):
			next(rotator)
	
	def test_1(self):
		rotator = Rotations([1])
		self.assertEqual(len(rotator), 1)
		self.assertSequenceEqual(next(rotator), [1])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_2(self):
		rotator = Rotations(['a',3.4])
		self.assertEqual(len(rotator), 2)
		self.assertSequenceEqual(next(rotator), ['a',3.4])
		self.assertSequenceEqual(next(rotator), [3.4,'a'])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3(self):
		rotator = Rotations([['a',1],3.4,'string'])
		self.assertEqual(len(rotator), 3)
		self.assertSequenceEqual(next(rotator),[['a',1],3.4,'string'])
		self.assertSequenceEqual(next(rotator), ['string',['a',1],3.4])
		self.assertSequenceEqual(next(rotator), [3.4,'string',['a',1]])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_step_type_error(self):
		with self.assertRaises(TypeError):
			next(Rotations([1,2,3],'string'))

	def test_5_step_2(self):
		rotator = Rotations([1,2,3,4,5], 2)
		self.assertEqual(len(rotator), 5)
		self.assertSequenceEqual(next(rotator), [1,2,3,4,5])
		self.assertSequenceEqual(next(rotator), [4,5,1,2,3])
		self.assertSequenceEqual(next(rotator), [2,3,4,5,1])
		self.assertSequenceEqual(next(rotator), [5,1,2,3,4])
		self.assertSequenceEqual(next(rotator), [3,4,5,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_4_step_2(self):
		rotator = Rotations([1,2,3,4], 2)
		self.assertEqual(len(rotator), 2)
		self.assertSequenceEqual(next(rotator), [1,2,3,4])
		self.assertSequenceEqual(next(rotator), [3,4,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3_step_0(self):
		rotator = Rotations([1,2,3], 0)
		self.assertEqual(len(rotator), 1)
		self.assertSequenceEqual(next(rotator), [1,2,3])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3_step_n1(self):
		rotator = Rotations([1,2,3], -1)
		self.assertEqual(len(rotator), 3)
		self.assertSequenceEqual(next(rotator), [1,2,3])
		self.assertSequenceEqual(next(rotator), [2,3,1])
		self.assertSequenceEqual(next(rotator), [3,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_5_step_n2(self):
		rotator = Rotations([1,2,3,4,5], -2)
		self.assertEqual(len(rotator), 5)
		self.assertSequenceEqual(next(rotator), [1,2,3,4,5])
		self.assertSequenceEqual(next(rotator), [3,4,5,1,2])
		self.assertSequenceEqual(next(rotator), [5,1,2,3,4])
		self.assertSequenceEqual(next(rotator), [2,3,4,5,1])
		self.assertSequenceEqual(next(rotator), [4,5,1,2,3])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_6_step_n2(self):
		rotator = Rotations([1,2,3,4,5,6], -2)
		self.assertEqual(len(rotator), 3)
		self.assertSequenceEqual(next(rotator), [1,2,3,4,5,6])
		self.assertSequenceEqual(next(rotator), [3,4,5,6,1,2])
		self.assertSequenceEqual(next(rotator), [5,6,1,2,3,4])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3_step_3(self):
		rotator = Rotations([1,2,3], 3)
		self.assertEqual(len(rotator), 1)
		self.assertSequenceEqual(next(rotator), [1,2,3])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3_step_n3(self):
		rotator = Rotations([1,2,3], -3)
		self.assertEqual(len(rotator), 1)
		self.assertSequenceEqual(next(rotator), [1,2,3])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3_step_4(self):
		rotator = Rotations([1,2,3], 4)
		self.assertEqual(len(rotator), 3)
		self.assertSequenceEqual(next(rotator), [1,2,3])
		self.assertSequenceEqual(next(rotator), [3,1,2])
		self.assertSequenceEqual(next(rotator), [2,3,1])
		with self.assertRaises(StopIteration):
			next(rotator)

	def test_3_step_n4(self):
		rotator = Rotations([1,2,3], -4)
		self.assertEqual(len(rotator), 3)
		self.assertSequenceEqual(next(rotator), [1,2,3])
		self.assertSequenceEqual(next(rotator), [2,3,1])
		self.assertSequenceEqual(next(rotator), [3,1,2])
		with self.assertRaises(StopIteration):
			next(rotator)