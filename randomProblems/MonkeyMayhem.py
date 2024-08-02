num_top, num_left = map(int, input().split())
left = [int(n) - m for m, n in enumerate(input().split())]
top = [int(n) for n in input().split()]

collisions = 0

for x, top_monkey in enumerate(top):
	if top_monkey != -1:
		length = len(left)
		left = list(filter(lambda a: a != top_monkey - x, left))
		collisions += length - len(left)

print(collisions)
