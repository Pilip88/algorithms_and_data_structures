# Time complexity is O(n^2)

def bubble_sort(a_list):
	for i in range(len(a_list)):
		swapped = False
		for j in range(0, len(a_list)-i-1):
			if a_list[j] > a_list[j+1]:
				a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
				swapped = True

		if not swapped:
			break

	return a_list