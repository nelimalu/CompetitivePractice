from random import randint, choice
import time


def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1


cases = [
	# batch 1
	# insert test case as a thing
	[10, randint(1,10)],
	[100, randint(1,50)],
	[1000, randint(50,100)],
	[1000, randint(100,200)],
	[1000, randint(300,400)],
	[1000, randint(400,500)],
	[1000, 800],
	[1000, 900],
	[1000, 1000],

	[10_000, randint(50,100)],
	[10_000, randint(5000,8000)],
	[10_000, 10_000],
	[50_000, randint(10_000,20_000)],
	[50_000, 50_000],
	[100_000, 10],
	[100_000, 1000],
	[100_000, 10_000],
	[100_000, 50_000],
	[100_000, 100_000],
] 


def generate_case():
	N = 100000 # randint(1,1000)
	P = 100000

	contestants = [x for x in range(N)]
	bet = [x for x in range(N)]

	start = time.time()
	for contestant in bet:
		a = binary_search(contestants, contestant)
	print("W/ BINARY SEARCH:", time.time() - start)

	'''
	start = time.time()
	for contestant in bet:
		a = contestants.index(contestant)
	print("W/OUT BINARY SEARCH:", time.time() - start)
	'''

generate_case()

for x, case in enumerate(cases):
	N = case[0]
	P = case[1]

	contestants = []
	for i in range(N):
		randval = randint(0, 1_000_000_000)
		while randval in contestants:
			randval = randint(0, 1_000_000_000)
		contestants.append(randval)

	contestants.sort()

	bet = []
	for i in range(P):
		c = choice(contestants)
		while c in bet:
			c = choice(contestants)
		if randint(1,1000) == 5:  # throw in -1 cases
			c = randint(0, 1_000_000_000)
		bet.append(c)

	solutions = [str(binary_search(contestants, b)) for b in bet]

	with open(f"testcases/{x + 1}.in", 'w') as file:
		file.write(str(N) + " " + str(P) + "\n" + "\n".join([str(v) for v in contestants]) + "\n" + "\n".join([str(v) for v in bet]) + "\n")

	with open(f"testcases/{x + 1}.out", 'w') as file:
		file.write("\n".join(solutions) + "\n")


	print(f"generated case {x + 1}/19")
