t = " ".join([input() for _ in range(int(input()))]).lower()
print("French" if t.count("s") >= t.count("t") else "English")
