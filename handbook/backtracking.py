n = 5


def solve(locations, level):
	if len(locations) == n:
		print(locations)
		return locations

	for x in range(n):
		if level == 0:
			locations.append((x, level))
			solve(locations, level + 1)
			locations.remove((x, level))
		else:
			for q in locations:
				if x == q[0] or x in [q[0] - (level - q[1]), q[0] + (level - q[1])]:
					break
			else:
				locations.append((x, level))
				solve(locations, level + 1)
				locations.remove((x, level))


solve([], 0)
