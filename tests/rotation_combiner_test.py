from unittest import TestCase
from rotation_combiner import Rotateable, RotationCombinations

class RotationCombinerTests(TestCase):

	def test_empty(self):
		iterator = RotationCombinations([])
		self.assertEqual(len(iterator), 1)
		self.assertSequenceEqual(next(iterator), [])
		with self.assertRaises(StopIteration):
			next(iterator)
	
	def test_1_empty(self):
		iterator = RotationCombinations([([],)])
		self.assertEqual(len(iterator), 1)
		self.assertSequenceEqual(next(iterator), [()])
		with self.assertRaises(StopIteration):
			next(iterator)

	def test_3_empty(self):
		iterator = RotationCombinations([([],),([],),([],)])
		self.assertEqual(len(iterator), 1)
		self.assertSequenceEqual(next(iterator), [(),(),()])
		with self.assertRaises(StopIteration):
			next(iterator)

	def test_3_singles(self):
		iterator = RotationCombinations([([1],),([2],),([3],)])
		self.assertEqual(len(iterator), 1)
		self.assertSequenceEqual(next(iterator), [(1,),(2,),(3,)])
		with self.assertRaises(StopIteration):
			next(iterator)

	def test_3_pairs(self):
		iterator = RotationCombinations([([1,2],),([3,4],),([5,6],)])
		self.assertEqual(len(iterator), 8)
		self.assertCountEqual(tuple(iterator),[
			((1,2),(3,4),(5,6)), 
			((1,2),(3,4),(6,5)), 
			((1,2),(4,3),(5,6)),
			((1,2),(4,3),(6,5)),
			((2,1),(3,4),(5,6)),
			((2,1),(3,4),(6,5)),
			((2,1),(4,3),(5,6)),
			((2,1),(4,3),(6,5))])
		
	def test_3_triples(self):
		iterator = RotationCombinations([([1,2,3],),([4,5,6],),([7,8,9],)])
		self.assertEqual(len(iterator), 27)
		self.assertCountEqual(tuple(iterator),[
			((1,2,3),(4,5,6),(7,8,9)),
			((2,3,1),(4,5,6),(7,8,9)),
			((3,1,2),(4,5,6),(7,8,9)),

			((1,2,3),(5,6,4),(7,8,9)),
			((2,3,1),(5,6,4),(7,8,9)),
			((3,1,2),(5,6,4),(7,8,9)),

			((1,2,3),(6,4,5),(7,8,9)),
			((2,3,1),(6,4,5),(7,8,9)),
			((3,1,2),(6,4,5),(7,8,9)),


			((1,2,3),(4,5,6),(8,9,7)),
			((2,3,1),(4,5,6),(8,9,7)),
			((3,1,2),(4,5,6),(8,9,7)),
			
			((1,2,3),(5,6,4),(8,9,7)),
			((2,3,1),(5,6,4),(8,9,7)),
			((3,1,2),(5,6,4),(8,9,7)),

			((1,2,3),(6,4,5),(8,9,7)),
			((2,3,1),(6,4,5),(8,9,7)),
			((3,1,2),(6,4,5),(8,9,7)),


			((1,2,3),(4,5,6),(9,7,8)),
			((2,3,1),(4,5,6),(9,7,8)),
			((3,1,2),(4,5,6),(9,7,8)),
			
			((1,2,3),(5,6,4),(9,7,8)),
			((2,3,1),(5,6,4),(9,7,8)),
			((3,1,2),(5,6,4),(9,7,8)),

			((1,2,3),(6,4,5),(9,7,8)),
			((2,3,1),(6,4,5),(9,7,8)),
			((3,1,2),(6,4,5),(9,7,8)),
		])

	def test_steps_3_2(self):
		iterator = RotationCombinations([([1,2,3,4,5,6],3),([7,8,9,10,11,12],2)])
		self.assertEqual(len(iterator), 6)
		self.assertCountEqual(tuple(iterator),[
			((1,2,3,4,5,6),(7,8,9,10,11,12)),
			((4,5,6,1,2,3),(7,8,9,10,11,12)),

			((1,2,3,4,5,6),(9,10,11,12,7,8)),
			((4,5,6,1,2,3),(9,10,11,12,7,8)),

			((1,2,3,4,5,6),(11,12,7,8,9,10)),
			((4,5,6,1,2,3),(11,12,7,8,9,10)),
		])

	def test_1_2_3(self):
		iterator = RotationCombinations([([1],),([2,3],),([4,5,6],)])
		self.assertEqual(len(iterator), 6)
		self.assertCountEqual(tuple(iterator),[
			((1,),(2,3),(4,5,6)),
			((1,),(3,2),(4,5,6)),

			((1,),(2,3),(5,6,4)),
			((1,),(3,2),(5,6,4)),

			((1,),(2,3),(6,4,5)),
			((1,),(3,2),(6,4,5)),
		])
	
	def test_rotateable_unpacking(self):
		args = ((1,2,3), -2)
		rotateable = Rotateable(*args)
		self.assertTupleEqual(args, (*rotateable,))
		self.assertTupleEqual(args, tuple(rotateable))
		self.assertEqual(rotateable, Rotateable(*rotateable))