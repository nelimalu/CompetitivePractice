import sys

N = int(sys.stdin.readline())

guesses = [sys.stdin.readline() for _ in range(N)]
answers = [sys.stdin.readline() for _ in range(N)]

counter = 0
for a, b in zip(guesses, answers):
	counter += int(a == b)

print(counter)
