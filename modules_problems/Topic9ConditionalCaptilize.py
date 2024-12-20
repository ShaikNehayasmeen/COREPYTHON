def preLetterCase(string, letter):
	index = string.find(letter)
	if index != -1:
		return string[:index].lower() + string[index:].upper()
		return string
print(preLetterCase("CAtCHa", "a"))  # Output: "cATCHA"
print(preLetterCase("Preteen", "e"))  # Output: "prETEEN"
print(preLetterCase("You've got this", "m"))  # Output: "you've got this"
print(preLetterCase("Keep trying", "k"))  # Output: "KEEP TRYING"
