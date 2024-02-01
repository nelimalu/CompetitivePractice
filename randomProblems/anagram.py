def a(word):
	return word.replace(" ", "")

print("Is an anagram." if sorted(a(input())) == sorted(a(input())) else "Is not an anagram.")
