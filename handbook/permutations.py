initial = [0, 1, 2]


def permutations(current: list):
	if len(current) == len(initial):
		print(*current)

	for i in initial:
		if i not in current:
			current.append(i)
			permutations(current)
			current.remove(i)



permutations([])
