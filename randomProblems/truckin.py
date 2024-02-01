import sys
# sys.setrecursionlimit(20)

min_daily = int(input())
max_daily = int(input())
num_extra = int(input())
stops = sorted([int(input()) for _ in range(num_extra)] + [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000])

def solve(position):
	print("::", stops[position])
	distance_to_end = 7000 - stops[position]
	if distance_to_end <= max_daily:
		if distance_to_end < min_daily:
			return 0
		return 1

	possible_stops = []

	for stop in stops[position + 1:]:
		if stop - stops[position] >= min_daily and stop - stops[position] <= max_daily:
			possible_stops.append(stop)
		if stop - stops[position] > max_daily:
			break

	print(possible_stops)

	num_branches = 0
	for stop in possible_stops:
		num_branches += solve(stops.index(stop))

	return num_branches


print(solve(0))
