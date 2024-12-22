def parse_hand(hand):
	cards = {
		"A": 0,
		"K": 0,
		"Q": 0,
		"J": 0,
		"T": 0,
		"9": 0,
		"8": 0,
		"7": 0,
		"6": 0,
		"5": 0,
		"4": 0,
		"3": 0,
		"2": 0
	}

	for card in hand:
		cards[card] += 1

	return cards


def classify(hand):
	amounts = list(hand.values())
	print(amounts)
	if 5 in amounts:
		return 0
	if 4 in amounts:
		return 1
	if 3 in amounts and 2 in amounts:
		return 2
	if 3 in amounts and 1 in amounts:
		return 3
	if amounts.count(2) == 2:
		return 4
	if 2 in amounts:
		return 5
	if 2 not in amounts and 3 not in amounts and 4 not in amounts and 5 not in amounts:
		return 6
	return -1


class Group:
	def __init__(self, hand, bid):
		self.raw_hand = hand
		self.hand = parse_hand(hand)
		self.bid = bid
		self.ranking = classify(self.hand)

	def __str__(self):
		return self.raw_hand


with open("../input.txt", 'r') as file:
	data = [Group(x.split()[0], int(x.split()[1])) for x in file.read().splitlines()]


ranking = [[], [], [], [], [], [], []]
convert = [
	"five of a kind",
	"four of a kind",
	"full house",
	"three of a kind",
	"two pair",
	"one pair",
	"high card"
]

values = {
	"A": 12,
	"K": 11,
	"Q": 10,
	"J": 9,
	"T": 8,
	"9": 7,
	"8": 6,
	"7": 5,
	"6": 4,
	"5": 3,
	"4": 2,
	"3": 1,
	"2": 0
}


def main():
	for hand in data:
		ranking[hand.ranking].append(hand)
		# print(convert[hand.ranking])
		print(hand)
	print(*[[str(y) for y in x] for x in ranking])

	for y, rank in enumerate(ranking):
		_sorted = rank[:]
		moved = True
		while moved:
			moved = False
			print(rank[:len(rank) - 1])
			for x, hand in enumerate(rank[:len(rank) - 1]):
				print(f"\nNEW HAND {x}\n")
				for i in range(5):
					print("COMPARE:")
					print(" ", str(rank[x])[i], str(rank[x + 1])[i])
					print(" ", values[str(rank[x])[i]], values[str(rank[x + 1])[i]])
					if values[str(rank[x])[i]] < values[str(rank[x + 1])[i]]:
						#print(*[[str(y) for y in x] for x in ranking])
						#print('hard time liek ajhsjdf')
						save = rank[x + 1]
						ranking[y][x + 1] = rank[x]
						ranking[y][x] = save
						
						moved = True
					print(" ", *[[str(y) for y in x] for x in ranking])
				break
			break
			

		ranking[y] = _sorted[:]

	total = 0
	merged = [j for i in ranking for j in i][::-1]
	for x, rank in enumerate(merged):
		total += merged.bid * x



main()