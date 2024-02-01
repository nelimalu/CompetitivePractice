num_opened = int(input())
boxes_opened = [int(input()) for _ in range(num_opened)]
offer = int(input())

possibilities = [100, 500, 1000, 5000, 10_000, 25_000, 50_000, 100_000, 500_000, 1_000_000]
total = sum(possibilities)

for box in boxes_opened:
	total -= possibilities[box - 1]


average = total / (10 - num_opened)

if offer > average:
	print("deal")
else:
	print("no deal")

