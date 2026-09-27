import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0]+matrix[1][1]
	det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	# x2 - trace*x +det =  0
	delta = trace*trace - 4*det
	if delta < 0:
		return None
	x1 = (trace+math.sqrt(delta)) / 2
	x2 = (trace-math.sqrt(delta))/2
	return [x1,x2]