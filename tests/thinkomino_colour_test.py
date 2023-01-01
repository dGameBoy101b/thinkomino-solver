from unittest import TestCase
from thinkomino_colour import ThinkominoColour

class ThinkominoColourTest(TestCase):
	def test_red(self):
		self.assertEqual(ThinkominoColour.RED.value, 'red')

	def test_orange(self):
		self.assertEqual(ThinkominoColour.ORANGE.value, 'orange')

	def test_yellow(self):
		self.assertEqual(ThinkominoColour.YELLOW.value, 'yellow')

	def test_green(self):
		self.assertEqual(ThinkominoColour.GREEN.value, 'green')

	def test_blue(self):
		self.assertEqual(ThinkominoColour.BLUE.value, 'blue')

	def test_purple(self):
		self.assertEqual(ThinkominoColour.PURPLE.value, 'purple')