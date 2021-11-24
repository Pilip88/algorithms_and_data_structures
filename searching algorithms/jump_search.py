import math
from linear_search import linear_search

def jump_search(a_list, item):
	len_of_list = len(a_list)
	jump_size = int(math.sqrt(len_of_list))
	i = 0

	while i < len_of_list and a_list[i] < item:
		if a_list[i+jump_size-1] == item:
			return i+jump_size-1
		elif a_list[i+jump_size-1] > item:
			lin_result = linear_search(a_list[i:i+jump_size-1], item)
			if lin_result > -1:
				return i + lin_result
			else:
				return lin_result
		i = i + jump_size

	lin_result = linear_search(a_list[i:i+jump_size], item)
	if lin_result > -1:
		return i + lin_result
	return lin_result
