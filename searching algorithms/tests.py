import unittest

from linear_search import linear_search, linear_search_2
from binary_search import binary_search, binary_search_recursive
from jump_search import jump_search

class SearchTests(unittest.TestCase):

	test_list = [3,23,1,33,5,341,222,1245,22,13,56,66,442,4123,4,100]
	test_list_sorted = [1, 3, 4, 5, 13, 23, 33, 56, 66, 100, 222, 341, 442, 1245, 4123]

	def test_linear_search(self):
		self.assertEqual(linear_search(self.test_list, 3), 0)
		self.assertEqual(linear_search(self.test_list, 33), 3)
		self.assertEqual(linear_search(self.test_list, 1245), 7)
		self.assertEqual(linear_search(self.test_list, 442), 12)
		self.assertEqual(linear_search(self.test_list, 100), 15)
		self.assertEqual(linear_search(self.test_list, 111), -1)
		self.assertEqual(linear_search(self.test_list, 333), -1)
		self.assertEqual(linear_search(self.test_list, 1111), -1)

	def test_linear_search_2(self):
		self.assertEqual(linear_search_2(self.test_list, 3), 0)
		self.assertEqual(linear_search_2(self.test_list, 33), 3)
		self.assertEqual(linear_search_2(self.test_list, 1245), 7)
		self.assertEqual(linear_search_2(self.test_list, 442), 12)
		self.assertEqual(linear_search_2(self.test_list, 100), 15)
		self.assertEqual(linear_search_2(self.test_list, 111), -1)
		self.assertEqual(linear_search_2(self.test_list, 333), -1)
		self.assertEqual(linear_search_2(self.test_list, 1111), -1)

	def test_binary_search(self):
		self.assertTrue(binary_search(self.test_list_sorted, 1))
		self.assertTrue(binary_search(self.test_list_sorted, 3))
		self.assertTrue(binary_search(self.test_list_sorted, 222))
		self.assertTrue(binary_search(self.test_list_sorted, 4123))
		self.assertFalse(binary_search(self.test_list_sorted, 6))
		self.assertFalse(binary_search(self.test_list_sorted, 1000))
		self.assertFalse(binary_search(self.test_list_sorted, 1111))

	def test_binary_search_recursive(self):
		self.assertTrue(binary_search_recursive(self.test_list_sorted, 1))
		self.assertTrue(binary_search_recursive(self.test_list_sorted, 3))
		self.assertTrue(binary_search_recursive(self.test_list_sorted, 222))
		self.assertTrue(binary_search_recursive(self.test_list_sorted, 4123))
		self.assertFalse(binary_search_recursive(self.test_list_sorted, 6))
		self.assertFalse(binary_search_recursive(self.test_list_sorted, 1000))
		self.assertFalse(binary_search_recursive(self.test_list_sorted, 1111))

	def test_jump_search(self):
		self.assertEqual(jump_search(self.test_list_sorted, 1), 0)
		self.assertEqual(jump_search(self.test_list_sorted, 3), 1)
		self.assertEqual(jump_search(self.test_list_sorted, 222), 10)
		self.assertEqual(jump_search(self.test_list_sorted, 4123), 14)
		self.assertEqual(jump_search(self.test_list_sorted, 6), -1)
		self.assertEqual(jump_search(self.test_list_sorted, 1000), -1)
		self.assertEqual(jump_search(self.test_list_sorted, 1111), -1)

if __name__ == "__main__":
	unittest.main()
