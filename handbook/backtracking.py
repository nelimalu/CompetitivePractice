n = 16
count = 0


def solve(locations, level):
	global count

	if len(locations) == n:
		count += 1
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
print(count)
