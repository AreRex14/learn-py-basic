class MyClass:
	variable = "blah"

	def function(self):
		print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# myobjectx.variable
print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()