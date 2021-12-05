import unittest

from selection_sort import selection_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

class SortingTests(unittest.TestCase):
	test_list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	test_list_2 = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
	test_list_3 = [1,4,2,3,19,18,5,6,20,17,11,10,7,8,12,14,9,13,15,16]

	def test_selection_sort(self):
		self.assertEqual(selection_sort(self.test_list_1), self.test_list_1)
		self.assertEqual(selection_sort(self.test_list_2), self.test_list_1)
		self.assertEqual(selection_sort(self.test_list_3), self.test_list_1)

	def test_bubble_sort(self):
		self.assertEqual(bubble_sort(self.test_list_1), self.test_list_1)
		self.assertEqual(bubble_sort(self.test_list_2), self.test_list_1)
		self.assertEqual(bubble_sort(self.test_list_3), self.test_list_1)

	def test_insertion_sort(self):
		self.assertEqual(insertion_sort(self.test_list_1), self.test_list_1)
		self.assertEqual(insertion_sort(self.test_list_2), self.test_list_1)
		self.assertEqual(insertion_sort(self.test_list_3), self.test_list_1)


if __name__ == "__main__":
	unittest.main()
