from math import sqrt


def isPrime(n, primes):
	if n in primes:
		return True

	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


def find_next_prime(last_prime, primes):
	counter = last_prime
	while True:
		counter += 1
		if isPrime(counter, primes):
			return counter
	return None


def main():
	primes = [1, 2, 3, 5]

	for i in range(int(input())):
		N = int(input())
		goal = N * 2

		counter = 1
		while True:
			if counter >= len(primes):
				primes.append(find_next_prime(primes[-1], primes))

			prime1 = primes[counter]
			prime2 = goal - prime1
			if isPrime(prime2, primes):
				print(prime1, prime2)
				break
				
			counter += 1


main()
