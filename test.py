def find_message(text):
	text = list(text)
	leight = len(text)
	i = 0
	while i < leight:
		word = str(text[i])
		i += 1
		if word.isupper() == True:
			mass=[]
			mass.append(word)

	mass = str(mass)
	return mass

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
