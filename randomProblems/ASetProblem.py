input()
N = [int(n) for n in input().split()]
M = [int(n) for n in input().split()]

count = 0
for number in M:
	if number in N:
		count += 1

print(count)
