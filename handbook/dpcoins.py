coins = [1, 3, 4]
n = 10

cache = {}


def solve(s):
	if s == 0:
		return 0
	if s < 0:
		return float("inf")
	if s in cache.keys():
		return cache[s]

	solutions = []
	for coin in coins:
		solutions.append(solve(s - coin) + 1)

	cache[s] = min(solutions)

	return cache[s]


print(solve(n))
