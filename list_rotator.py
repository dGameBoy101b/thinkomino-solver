from typing import Iterator

def rotate_list(ls:list, step:int=1, iterations:int=None)->Iterator[list]:
	#empty special case
	if (len(ls) < 1):
		return
	#process step parameter
	try:
		step = int(step)
	except ValueError as x:
		raise TypeError('step must be an integer', x)
	if step < 1:
		raise ValueError('step must be 1 or greater')
	if step > len(ls):
		raise ValueError(f'step must be lesser than or equal to the length of the list ({len(ls)})')
	#process iterations parameter
	if iterations is None:
		iterations = len(ls)
	try:
		iterations = int(iterations)
	except ValueError as x:
		raise TypeError('iterations must be an integer', x)
	if iterations < 0:
		raise ValueError('iterations must be 0 or greater')
	#generate rotations
	for i in range(iterations):
		yield ls
		ls = ls[-step:] + ls[:-step]
	return
