from unittest import TestCase
from dictionary_xml_builder import DictionaryXMLBuilder
from xml.etree.ElementTree import XMLParser

class DictionaryXMLBuilderTest(TestCase):

	def setUp(self) -> None:
		self.parser = XMLParser(target=DictionaryXMLBuilder())

	def test_empty(self):
		TAG = 'root'
		self.parser.feed(f'<{TAG}></{TAG}>')
		self.assertDictEqual(self.parser.close(), {TAG: dict()})

	def test_single_value(self):
		TAG = 'root'
		VALUE = 'test value'
		self.parser.feed(f'<{TAG}>{VALUE}</{TAG}>')
		self.assertDictEqual(self.parser.close(), {TAG: VALUE})

	def test_single_nested_empty(self):
		ROOT_TAG = 'root'
		INNER_TAG = 'inner'
		self.parser.feed(f'<{ROOT_TAG}><{INNER_TAG}></{INNER_TAG}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {INNER_TAG: dict()}})

	def test_single_nested_value(self):
		ROOT_TAG = 'root'
		INNER_TAG = 'inner'
		VALUE = 'test value'
		self.parser.feed(f'<{ROOT_TAG}><{INNER_TAG}>{VALUE}</{INNER_TAG}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {INNER_TAG: VALUE}})

	def test_multiple_nested_empty(self):
		ROOT_TAG = 'root'
		INNER_TAG1 = 'inner1'
		INNER_TAG2 = 'inner2'
		INNER_TAG3 = 'inner3'
		self.parser.feed(f'<{ROOT_TAG}><{INNER_TAG1}></{INNER_TAG1}><{INNER_TAG2}></{INNER_TAG2}><{INNER_TAG3}></{INNER_TAG3}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {INNER_TAG1: dict(), INNER_TAG2: dict(), INNER_TAG3: dict()}})

	def test_multiple_nested_value(self):
		ROOT_TAG = 'root'
		INNER_TAG1 = 'inner1'
		VALUE1 = 'value1'
		INNER_TAG2 = 'inner2'
		VALUE2 = 'value2'
		INNER_TAG3 = 'inner3'
		VALUE3 = 'inner3'
		self.parser.feed(f'<{ROOT_TAG}><{INNER_TAG1}>{VALUE1}</{INNER_TAG1}><{INNER_TAG2}>{VALUE2}</{INNER_TAG2}><{INNER_TAG3}>{VALUE3}</{INNER_TAG3}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {INNER_TAG1: VALUE1, INNER_TAG2: VALUE2, INNER_TAG3: VALUE3}})

	def test_single_many_level_empty(self):
		ROOT_TAG = 'root'
		OUTER_TAG = 'outer'
		INNER_TAG = 'inner'
		self.parser.feed(f'<{ROOT_TAG}><{OUTER_TAG}><{INNER_TAG}></{INNER_TAG}></{OUTER_TAG}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {OUTER_TAG: {INNER_TAG: dict()}}})

	def test_single_many_level_value(self):
		ROOT_TAG = 'root'
		OUTER_TAG = 'outer'
		INNER_TAG = 'inner'
		VALUE = 'test value'
		self.parser.feed(f'<{ROOT_TAG}><{OUTER_TAG}><{INNER_TAG}>{VALUE}</{INNER_TAG}></{OUTER_TAG}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {OUTER_TAG: {INNER_TAG: VALUE}}})

	def test_multiple_many_level_empty(self):
		ROOT_TAG = 'root'
		OUTER_TAG1 = 'outer1'
		OUTER_TAG2 = 'outer2'
		INNER_TAG1 = 'inner1'
		INNER_TAG2 = 'inner2'
		INNER_TAG3 = 'inner3'
		INNER_TAG4 = 'inner4'
		self.parser.feed(f'<{ROOT_TAG}><{OUTER_TAG1}><{INNER_TAG1}></{INNER_TAG1}><{INNER_TAG2}></{INNER_TAG2}></{OUTER_TAG1}><{OUTER_TAG2}><{INNER_TAG3}></{INNER_TAG3}><{INNER_TAG4}></{INNER_TAG4}></{OUTER_TAG2}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {OUTER_TAG1: {INNER_TAG1: dict(), INNER_TAG2: dict()}, OUTER_TAG2: {INNER_TAG3: dict(), INNER_TAG4: dict()}}})

	def test_multiple_many_level_value(self):
		ROOT_TAG = 'root'
		OUTER_TAG1 = 'outer1'
		OUTER_TAG2 = 'outer2'
		INNER_TAG1 = 'inner1'
		INNER_TAG2 = 'inner2'
		INNER_TAG3 = 'inner3'
		INNER_TAG4 = 'inner4'
		VALUE1 = 'value1'
		VALUE2 = 'value2'
		VALUE3 = 'value3'
		VALUE4 = 'value4'
		self.parser.feed(f'<{ROOT_TAG}><{OUTER_TAG1}><{INNER_TAG1}>{VALUE1}</{INNER_TAG1}><{INNER_TAG2}>{VALUE2}</{INNER_TAG2}></{OUTER_TAG1}><{OUTER_TAG2}><{INNER_TAG3}>{VALUE3}</{INNER_TAG3}><{INNER_TAG4}>{VALUE4}</{INNER_TAG4}></{OUTER_TAG2}></{ROOT_TAG}>')
		self.assertDictEqual(self.parser.close(), {ROOT_TAG: {OUTER_TAG1: {INNER_TAG1: VALUE1, INNER_TAG2: VALUE2}, OUTER_TAG2: {INNER_TAG3: VALUE3, INNER_TAG4: VALUE4}}})
