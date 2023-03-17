import unittest
from fastModularExponentiation import getPowerOfTwoModC, fastModularExponentiation


class FastPowByModuleTest(unittest.TestCase):
	def test1(self):
		base = 1
		degree = 1
		module = 1
		expected = 0
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test2(self):
		base = 12345
		degree = 1234
		module = 13
		expected = 12
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test3(self):
		base = 12345
		degree = 12345
		module = 13
		expected = 8
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test4(self):
		base = 12345
		degree = 123456
		module = 13
		expected = 1
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test5(self):
		base = 12345
		degree = 1234
		module = 133
		expected = 81
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test6(self):
		base = 12345
		degree = 1234
		module = 1333
		expected = 231
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test7(self):
		base = 12345
		degree = 1234
		module = 13335
		expected = 3315
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test8(self):
		base = 12345
		degree = 12345
		module = 133
		expected = 50
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test9(self):
		base = 12345
		degree = 12345
		module = 1333
		expected = 342
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test10(self):
		base = 12345
		degree = 12345
		module = 13335
		expected = 8730
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test11(self):
		base = 12345
		degree = 123456
		module = 133
		expected = 106
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test12(self):
		base = 12345
		degree = 123456
		module = 1333
		expected = 686
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test13(self):
		base = 12345
		degree = 123456
		module = 13335
		expected = 12090
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test14(self):
		base = 12345
		degree = 123456
		module = 133353
		expected = 17955
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test15(self):
		base = 1234567891011121314151617181920
		degree = 1234567891011121314151617181921
		module = 1234567891011121314151617181922
		expected = 555812583000353450709029951878
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test16(self):
		base = 1234567891011121314151617181920
		degree = 1234567891011121314151617181921
		module = 1
		expected = 0
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)

	def test17(self):
		base = 31
		degree = 123456789101112131415161718192122232425262728293031
		module = 987654321
		expected = 215367226
		actual = fastModularExponentiation(base, degree, module)
		self.assertEqual(expected, actual)


if __name__ == '__main__':
	unittest.main()
