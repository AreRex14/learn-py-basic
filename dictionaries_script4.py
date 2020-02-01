# removing a specified index
phonebook = {
	"John" : 111234567,
    "Jack" : 121234567,
    "Mary" : 131234567
}
del phonebook["John"] # or phonebook.pop("John")
print(phonebook)