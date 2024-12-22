from math import sqrt

a, b, n = map(int, input().split())


def get_common_factors(number):
	factors = set()
	for i in range(1, int(sqrt(number)) + 1):
		if number % i == 0:
			factors.add(i)
			factors.add(number // i)
	factors.add(number)
	return factors


a_factors = get_common_factors(a)
b_factors = get_common_factors(b)
intersection = a_factors.intersection(b_factors)

print(*sorted(list(intersection))[-n:])
