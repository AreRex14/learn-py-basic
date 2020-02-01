# Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of the values stored in it.
phonebook = {"John" : 111234567, "Jack" : 121234567, "Mary" : 131234567}
for name, number in phonebook.items():
	print("Phone number of %s is %d" % (name, number))