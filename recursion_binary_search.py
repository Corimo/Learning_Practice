search_list = [1, 2, 4, 6, 8]

looking_for = int(input("Please enter number to search: "))

#def bin_convert (search_number, group):
#	bin_search (search_number, group, 0, len (group) - 1)

def bin_search (search_number, list_of_numbers, low, high):
	if high >= low:
		mid = ((high + low) // 2)

		if list_of_numbers[mid] == search_number:
			return mid

		elif search_number > list_of_numbers[mid]:
			return bin_search(search_number, list_of_numbers, mid + 1, high)

		elif search_number < list_of_numbers[mid]:
			return bin_search (search_number, list_of_numbers, low, mid - 1)

	else:
		return -1

print (bin_search (looking_for, search_list, 0, len(search_list) - 1))