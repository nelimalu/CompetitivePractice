weights = [1,3,3,5]
possible = [0]


for weight in weights:
	for p in range(len(possible)):
		if possible[p] + weight not in possible:
			possible.append(possible[p] + weight)
	if weight not in possible:
		possible.append(weight)


print(possible)
