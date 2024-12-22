import sys
sys.setrecursionlimit(10000)

rows, cols, limit = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(rows)]
movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_neighbours(x, y):
	neighbours = [-1, -1, -1, -1]

	if x - 1 >= 0:
		neighbours[0] = grid[y][x - 1]
	if x + 1 < cols:
		neighbours[1] = grid[y][x + 1]
	if y - 1 >= 0:
		neighbours[2] = grid[y - 1][x]
	if y + 1 < rows:
		neighbours[3] = grid[y + 1][x]

	return neighbours


def move(x, y, value, last_cookie, depth):
	if depth == limit:
		value += grid[y][x]
		return value

	neighbours = get_neighbours(x, y)

	highest = 0

	if grid[y][x] > last_cookie:
		a = move(0, 0, value + grid[y][x], grid[y][x], depth + 1)
		if a > highest:
			highest = a

	for a, neighbour in enumerate(neighbours):
		if neighbour >= 0:
			a = move(x + movement[a][0], y + movement[a][1], value, last_cookie, depth + 1)
			if a > highest:
				highest = a

	return highest


print(move(0, 0, 0, 0, 0))
