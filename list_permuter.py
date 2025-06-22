from typing import Iterator

def permute_list(ls:list)->Iterator[list]:
	#empty/single special case
	if len(ls) < 2:
		yield ls
		return
	#generate permutations
	for index in range(len(ls)):
		for permute in permute_list(ls[1:]):
			yield permute[:index] + [ls[0]] + permute[index:]
