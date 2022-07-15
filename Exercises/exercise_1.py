# EXERCISE-1
words = input("Enter Words: ").lower().split(" ") 
unique_words = []
occ = []

for i in words:
	if not i in unique_words and i.isalpha():
		unique_words.append(i)	

for w in unique_words:
	c = words.count(w)
	occ.append(str(c))

print(len(unique_words))
print(" ".join(occ))