values = [int(n) for n in input().split()]

psa = [values[0]]

# -1 2 4 -3 5 2 -5 2
max_index = 0
current_max = 0
for x, i in enumerate(values[1:]):
	next_value = psa[x] + i
	if next_value > current_max:
		current_max = next_value
		max_index = x + 1
	psa.append(next_value)

start_index = 0
for x, i in enumerate(psa[:max_index][::-1]):
	if i <= 0:
		start_index = max_index - (x)
		break


print(values[start_index:max_index + 1])
