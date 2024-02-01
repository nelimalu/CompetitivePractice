import sys
import bisect

num_integers, num_queries = map(int, sys.stdin.readline().split())

numbers = sorted([int(n) for n in sys.stdin.readline().split()])
queries = [int(sys.stdin.readline()) for _ in range(num_queries)]
queried = []

cache = {}


def bsearch(array, value, left=0):
	right = len(array) - 1
	index = len(array) // 2

	if len(array) == 0 or value < array[left]:
		return 0
	if value > array[right]:
		return len(array)

	while True:
		if value < array[index]:
			right = index
			index = (left + right) // 2
		elif value > array[index]:
			left = index
			index = (left + right) // 2
		else:
			return index

		if right - left <= 1:
			return right

#print()
#print(numbers)

for query in queries:
	if query not in cache:  # might be slower
		low = 0
		'''
		queried_index = bsearch(queried, query)
		queried.insert(queried_index, query)

		low_index = 0
		low = 0
		if queried_index > 0:
			low_index = queried[queried_index - 1]
			low = cache[low_index] - 1 # might need to subtract 1 aaas

		# print("LOW:", low)
		'''
		if query in numbers:
			cache[query] = numbers.index(query)
		else:
			cache[query] = bisect.bisect(numbers, query)

	
	print(cache[query])
