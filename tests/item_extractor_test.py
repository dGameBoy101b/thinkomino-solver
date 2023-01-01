from unittest import TestCase
from item_extractor import extract_item

class ConnectedListMapperTest(TestCase):

	def test_flat_index(self):
		self.assertEqual(extract_item([1,2,3], [0]), 1)

	def test_nested_indices(self):
		self.assertEqual(extract_item([[1,2,3],[4,5,6],[7,8,9]], [2,0]), 7)

	def test_flat_key(self):
		self.assertEqual(extract_item({'a':1,'b':2,'c':3}, ['c']), 3)

	def test_nested_keys(self):
		self.assertEqual(extract_item({'a':{'b':1,'c':2,'d':3},'e':{'f':4,'g':5,'h':6},'i':{'j':7,'k':8,'l':9}}, ['e','h']), 6)

	def test_nested_mixed(self):
		self.assertEqual(extract_item([{'a':1,'b':2,'c':3},{'d':4,'e':5,'f':6},{'g':7,'h':8,'i':9}], [0,'b']), 2)
		self.assertEqual(extract_item({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}, ['a',1]), 2)