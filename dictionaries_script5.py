# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {
	"John" : 111234567,
    "Jack" : 121234567,
    "Mary" : 131234567
}
# write your code here
phonebook.update({"Jake" : 1234567111})
phonebook.pop("Mary")

# testing code
if "Jake" in phonebook:
	print("Jake is listed in the phonebook.")
if "Mary" not in phonebook:
	print("Mary is not listed in the phonebook.")