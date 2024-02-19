from math import sqrt
from collections import deque

rows = int(input())
cols = int(input())
END = (rows - 1, cols - 1)


def get_factors(n):
	factors = []
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			factors.append((i - 1, n // i - 1))
			factors.append((n // i - 1, i - 1))

	return factors


factors = {}
grid = [[int(m) for m in input().split()] for _ in range(rows)]
visited = set()
queue = deque([(0, 0)])

possible = False

while not possible and len(queue) > 0:

	current_loc = queue.popleft()
	visited.add(current_loc)
	current_val = grid[current_loc[0]][current_loc[1]]

	if current_val in factors:
		current_factors = factors[current_val]
	else:
		current_factors = get_factors(current_val)
		factors[current_val] = current_factors

	for factor in current_factors:
		if factor == END:
			possible = True
			break
		if factor[0] < rows and factor[1] < cols and factor not in visited:
			queue.append(factor)


print("yes" if possible else "no")

