import sys

num_jerseys = int(sys.stdin.readline())
num_athletes = int(sys.stdin.readline())

jerseys = [input() for _ in range(num_jerseys)]
size_to_array = ["S", "M", "L"]
requests = [
	[],
	[],
	[]
]

for i in range(num_athletes):
	a, b = sys.stdin.readline().split()
	requests[size_to_array.index(a)].append(int(b))  # remove int?

count = 0
for s, size in enumerate(requests):
	for requested_num in size:
		if jerseys[requested_num - 1] is not None:
			if size_to_array.index(jerseys[requested_num - 1]) >= s:
				count += 1
				jerseys[requested_num - 1] = None

print(count)


