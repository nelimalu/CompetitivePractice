n = int(input())
count = 0


def find_neighbours(point):
	x, y = point
	neighbours = []

	if y - 1 >= 0:
		neighbours.append((x, y - 1))
	if y + 1 < n:
		neighbours.append((x, y + 1))
	if x - 1 >= 0:
		neighbours.append((x - 1, y))
	if x + 1 < n:
		neighbours.append((x + 1, y))

	return neighbours


def solve(path):
	global count

	if path[-1] == (n - 1, n - 1):
		if len(path) == n ** 2:
			count += 1
		return

	if path[-1] == (0,0):
		path.append((0,1))
		solve(path)
		path.remove((0,1))
		return

	x, y = path[-1]
	neighbours = find_neighbours(path[-1])
	if neighbours == [(x - 1, y), (x + 1, y)] or neighbours == [(x, y - 1), (x, y + 1)]:
		return
	for neighbour in neighbours:
		if neighbour not in path:
			path.append(neighbour)
			solve(path)
			path.remove(neighbour)



solve([(0,0)])
print(count * 2)
