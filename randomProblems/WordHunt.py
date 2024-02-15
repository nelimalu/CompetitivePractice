word = input()
rows = int(input())
cols = int(input())

maze = [input().split() for _ in range(rows)]

total = 0


def get_neighbours(x, y):  # can be made more efficient
	neighbours = []
	if y - 1 >= 0:
		neighbours.append((y - 1, x))
		if x - 1 >= 0:
			neighbours.append((y - 1, x - 1))
		if x + 1 < cols:
			neighbours.append((y - 1, x + 1))

	if y + 1 < rows:
		neighbours.append((y + 1, x))
		if x - 1 >= 0:
			neighbours.append((y + 1, x - 1))
		if x + 1 < cols:
			neighbours.append((y + 1, x + 1))

	if x - 1 >= 0:
		neighbours.append((y, x - 1))
	if x + 1 < cols:
		neighbours.append((y, x + 1))

	return neighbours


def ninety(direction):
	if direction[0] == 0:
		return [(-1, 0), (1, 0)]
	if direction[1] == 0:
		return [(0, 1), (0, -1)]
	if direction in ((1, 1), (-1, -1)):
		return [(1, -1), (-1, 1)]
	if direction in ((1, -1), (-1, 1)):
		return [(1, 1), (-1, -1)]


def deep_search(y, x, d, turned, history):
	global total

	if len(history) == len(word):
		return

	directions = [d]
	if not turned:
		directions += ninety(d)
	print(directions)
	for a, direction in directions:
		next_x = x + direction[0]
		next_y = y + direction[1]
		if next_x < 0 or next_x >= cols or next_y < 0 or next_y >= rows:
			return 0

		# print(f"-- {history}, {x}, {y}, {maze[y][x]}, {len(directions)} --")
		# print(maze[y][x], maze[next_y][next_x], word[len(history)])
		# print(history)
		if maze[next_y][next_x] == word[len(history)]:
			new_history = history + maze[next_y][next_x]

			if len(new_history) == len(word):
				# print("+++++++++")
				total += 1
			deep_search(next_y, next_x, direction, True if a > 0 else turned, new_history)


def start_search(x, y):
	for neighbour in get_neighbours(x, y):
		if maze[neighbour[0]][neighbour[1]] == word[1]:
			direction = (neighbour[1] - x, neighbour[0] - y)
			deep_search(*neighbour, direction, False, word[:2])


def main():
	for y, row in enumerate(maze):
		for x, letter in enumerate(row):
			if letter == word[0]:
				start_search(x, y)
	print(total)


main()
