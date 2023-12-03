num_letters, consonant_limit, vowel_limit = map(int, input().split())
word = input()
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"

for i in range(num_letters):
	try:
		consonant_count = 0
		for letter in word[i:i + consonant_limit + 1]:
			if letter in consonants:
				consonant_count += 1
		if consonant_count > consonant_limit:
			print("NO")
			quit()
	except IndexError:
		pass

	try:
		vowel_count = 0
		for letter in word[i:i + vowel_limit + 1]:
			if letter in vowels:
				vowel_count += 1
		if vowel_count > vowel_limit:
			print("NO")
			quit()
	except IndexError:
		pass

print("YES")
