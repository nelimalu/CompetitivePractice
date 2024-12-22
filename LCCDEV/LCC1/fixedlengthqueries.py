# num_values, num_queries = map(int, input().split())
# arr = [int(n) for n in input().split()]
# queries = [int(input()) for n in range(num_queries)]
from collections import deque

def solve(arr, queries):
	out = []
	
	for q in queries:
		min_maxima = float('inf')
		stack = deque(arr[:q])
		current_max = max(arr[:q])
		for i in range(q - 1, len(arr)):
			if current_max < min_maxima:
				min_maxima = current_max
			if i == len(arr) - 1:
				break
			stack.append(arr[i + 1])
			if stack[-1] > current_max:
				current_max = stack[-1]
			a = stack.popleft()
			if a == current_max:
				current_max = max(list(stack))			
		out.append(min_maxima)
	return out


print(solve([33, 11, 44, 11, 55], [1, 2, 3, 4, 5]))
