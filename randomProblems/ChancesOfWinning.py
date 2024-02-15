favourite = int(input()) - 1
played = int(input())
points = [0, 0, 0, 0]
#   teams 1, 2, 3, 4

matchups = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
past = []

for i in range(int(played)):
	team1, team2, points1, points2 = map(int, input().split())
	if tuple(sorted([team1 - 1, team2 - 1])) in matchups:
		matchups.remove(tuple(sorted([team1 - 1, team2 - 1])))

	if points1 > points2:
		points[team1 - 1] += 3
	elif points2 > points1:
		points[team2 - 1] += 3
	else:
		points[team1 - 1] += 1
		points[team2 - 1] += 1


def solve(_points, _matches):
	print("-- first layer --" if len(_matches) == 2 else "-- second layer --")
	print(_points, _matches)


	if len(_matches) == 0 and \
		_points[favourite] == max(_points) and \
		len([x for x in _points if x == _points[favourite]]) == 1:

		return 1

	output = 0
	for match in _matches:
		for i in range(2):
			p = _points[:]
			p[match[0]] += 3
			output += solve(p, [x for x in _matches if x != match])

		p = _points[:]
		p[match[0]] += 1
		p[match[1]] += 1
		output += solve(p, [x for x in _matches if x != match])

	return output


print(matchups)
print(solve(points[:], matchups[:]))
