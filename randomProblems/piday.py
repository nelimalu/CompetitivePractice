import sys
n = int(sys.stdin.readline())  # pies
k = int(sys.stdin.readline())  # people

cache = {}


def possibleAfter(currentSum, currentLength, lastElement):
	if (currentSum, currentLength, lastElement) in cache:
		return cache[(currentSum, currentLength, lastElement)]

	if currentLength == k:
		if currentSum < n:
			return 0
		else:
			return 1 

	stepsLeft = k - currentLength
	piesLeft = n - currentSum

	max_possible = int(piesLeft / stepsLeft)  # problem here probably

	if currentLength == 0:
		min_possible = 1
	else:
		if max_possible < lastElement:
			return 0

		if currentLength == k - 1:
			min_possible = piesLeft
		else:
			min_possible = lastElement

	# print(min_possible, max_possible)

	possibilities = 0
	for i in range(min_possible, max_possible + 1):
		possibilities += possibleAfter(currentSum + i, currentLength + 1, i)

	cache[(currentSum, currentLength, lastElement)] = possibilities
	return possibilities


print(possibleAfter(0, 0, 0))

