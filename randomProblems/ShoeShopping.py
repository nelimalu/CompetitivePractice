input()
shoes = [int(x) for x in input().split()]


def three(arr):
	copy = arr[:]
	copy.remove(min(copy))
	return sum(copy)


def get_minimum(arr):
	if len(arr) == 0:
		return 0
	if len(arr) == 1:
		return arr[0]

	previous = arr[:-1]
	current = arr[-1]

	prev_mins = [
		get_minimum(previous),
		get_minimum(previous[:-1]),
		get_minimum(previous[:-2])
	]

	#print("--start run--")
	#print("current:", current)
	#print("previous:", prev_mins)

	minimums = []
	for x, i in enumerate(prev_mins):
		#if i is None:
		#	break
		
		if x == 0:
			minimums.append(i + current)

		if x == 1:
			minimums.append(i + max(current, arr[-2]) + (min(current, arr[-2]) / 2))

		if x == 2 and 0 not in prev_mins:
			# print("fuck you")
			minimums.append(i + three(arr[-3:]))

	if len(minimums) == 0:
		return current

	#print("options:", minimums)
	#print("--end run--")

	return min(minimums)


print(float("{0:.1f}".format(get_minimum(shoes))))
