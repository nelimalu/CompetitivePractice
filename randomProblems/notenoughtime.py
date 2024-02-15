import sys

N = int(input())  # customers
T = int(input())  # time

customers = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]


for i in range(N):
	
