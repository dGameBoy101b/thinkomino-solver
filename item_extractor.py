def extract_item(ls:list, key_sequence:list)->object:
	item = ls
	for key in key_sequence:
		item = item[key]
	return item
