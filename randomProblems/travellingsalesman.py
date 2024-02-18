from collections import deque

num_cities, num_roads = map(int, input().split())

roads = {}
for i in range(num_roads):
	a, b = map(int, input().split())

	if a in roads:
		roads[a].append(b)
	else:
		roads[a] = [b]

	if b in roads:
		roads[b].append(a)
	else:
		roads[b] = [a]

queue = deque([int(input()) for _ in range(int(input()))])
visited = set()

counter = -1
while len(queue) > 0:
	# print(visited, queue)

	for i in range(len(queue)):
		item = queue.popleft()

		visited.add(item)
		for city in roads[item]:
			if city not in visited and city not in queue:
				queue.append(city)
	
	counter += 1


'''
11 11
1 2
2 8
2 9
9 10
1 3
11 3
1 4
4 6
4 5
5 7
7 11
2
10
11

answer: 4
'''


print(counter)
