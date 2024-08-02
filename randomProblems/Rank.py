num_players, games_played = map(int, input().split())

to_win = {}
cyclic_players = set()


def add(first, second):
	global to_win

	if first in to_win:
		to_win[first].append(second)
	else:
		to_win[first] = [second]


for i in range(num_players):
	p1, p2, s1, s2 = map(int, input().split())
	if s1 > s2:
		add(p1, p2)  # put p2 in p1 win list
	else:
		add(p2, p1)


def search(player, goal, depth):
	if player == goal:
		return depth

	cyclic = []
	for wins in to_win[player]:
		for other_player in wins:
			cyclic.append(search(other_player, goal, (depth + [player]).copy()))

	return cyclic


for player in to_win.keys():
	for win in to_win[player]:
		cyclic_players.update(set(search(win, player, [])))

print(len(list(cyclic_players)))


