from unittest import TestCase
from list_permuter import permute_list

class ListPermuterTest(TestCase):

	def test_empty(self):
		permuter = permute_list([])
		self.assertEqual(next(permuter), [])
		with self.assertRaises(StopIteration):
			next(permuter)

	def test_one(self):
		permuter = permute_list([1])
		self.assertEqual(next(permuter), [1])
		with self.assertRaises(StopIteration):
			next(permuter)

	def test_two(self):
		permuter = permute_list(['a',3.4])
		self.assertEqual(next(permuter), ['a',3.4])
		self.assertEqual(next(permuter), [3.4, 'a'])
		with self.assertRaises(StopIteration):
			next(permuter)

	def test_three(self):
		permuter = permute_list([['a',1], 3.4, 'string'])
		self.assertEqual(next(permuter), [['a',1],3.4,'string'])
		results = [x for x in permuter]
		self.assertCountEqual(results, (
			[['a',1],'string',3.4], 
			[3.4,['a',1],'string'],
			[3.4,'string',['a',1]], 
			['string',['a',1],3.4],
			['string',3.4,['a',1]]), results)
