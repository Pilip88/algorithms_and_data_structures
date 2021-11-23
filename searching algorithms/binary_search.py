# Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

def binary_search(sorted_list, item):
	first_index = 0
	last_index = len(sorted_list) - 1
	found = False

	while not found and first_index <= last_index:
		midpoint = (last_index + first_index) // 2
		if sorted_list[midpoint] == item:
			found = True
		else:
			if sorted_list[midpoint] < item:
				first_index = midpoint + 1
			else:
				last_index = midpoint - 1

	if found:
		return True
	return False
