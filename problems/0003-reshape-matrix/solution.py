import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	m = len(a)
	n = len(a[0]) if m > 0 else 0
	mm,nn = new_shape
	if mm*nn != m*n:
		return []

	reshaped_matrix = [[0 for _ in range(nn)] for _ in range(mm)]
	x,y = 0,0
	for i in range(mm):
		for j in range(nn):
			reshaped_matrix[i][j] = a[x][y]
			y += 1
			if y == n:
				y = 0
				x += 1
	return reshaped_matrix