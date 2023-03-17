import unittest
from extendedEuclideanAlgorithm import extendedEuclideanAlgorithm as targetFunc


class targetFuncTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(targetFunc(240, 46), (2, -9, 47))

	def test2(self):
		self.assertEqual(targetFunc(30, 18), (6, -1, 2))

	def test3(self):
		self.assertEqual(targetFunc(0, 0), (0, 0, 1))

	def test4(self):
		self.assertEqual(targetFunc(4584, 21), (3, -3, 655))

	def test5(self):
		self.assertEqual(targetFunc(4584723823883294, 34873271244), (14, -71768291, 9435243147822))

	def test6(self):
		self.assertEqual(targetFunc(9985839522374633142, 3287444352), (6, -20780039, 63120805253005922))



if __name__ == '__main__':
	unittest.main()
