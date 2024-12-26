grid = [
	[3, 7, 9, 2, 7],
	[9, 8, 3, 5, 5],
	[1, 7, 9, 8, 5],
	[3, 8, 6, 4, 10],
	[6, 3, 9, 7, 8]
]


def cheapest(x, y):
	if x < 0 or y < 0:
		return float('inf')
	if x == 0 and y == 0:
		return grid[y][x]
	return min(cheapest(x - 1, y), cheapest(x, y - 1)) + grid[y][x]


print(cheapest(4, 4))
