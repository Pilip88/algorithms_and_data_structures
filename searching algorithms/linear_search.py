# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
# Time complexity is O(n)

def linear_search(a_list, item):
	current_index = 0
	found = False

	while current_index < len(a_list) and not found:
		if item == a_list[current_index]:
			found = True
		else:
			current_index = current_index + 1

	if found:
		return current_index
	else:
		return -1

def linear_search_2(a_list, item):
	current_index = 0
	for element in a_list:
		if element == item:
			return current_index
		else:
			current_index = current_index + 1
	return -1
