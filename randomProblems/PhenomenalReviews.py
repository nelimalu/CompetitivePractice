num_restaurants, num_pho = map(int, input().split())
pho_locs = [int(x) for x in input().split()]

tree = {}


class Travel:
	def __init__(self, phos_encountered, distance):
		self.phos_encountered = phos_encountered
		self.distance = distance


for _ in range(num_restaurants - 1):
	a, b = map(int, input().split())

	if a not in tree:
		tree[a] = [b]
	elif b not in tree[a]:
		tree[a].append(b)

	if b not in tree:
		tree[b] = [a]
	elif a not in tree[b]:
		tree[b].append(a)

print("---")

def search(loc, prev_loc, depth):
	children = tree[loc]

	print(loc, depth, ":")

	if len(children) == 1 and prev_loc != loc:
		return Travel(int(loc in pho_locs), 1)

	current_travel = Travel(int(loc in pho_locs), 1)

	for child in children:
		if child != prev_loc:
			result = search(child, loc, depth + 1)
			if result.phos_encountered > 0:
				current_travel.phos_encountered += result.phos_encountered
				current_travel.distance += result.distance

	print("   ", loc, current_travel.phos_encountered, current_travel.distance)

	return current_travel

a = search(pho_locs[0], pho_locs[0], 0).distance
print("---")
print(a)
