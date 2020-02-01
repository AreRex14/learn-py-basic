def linux_interaction():
	assert ('linux' in sys.platform), "Function can only run in linux."
	print('Doing something')

# avoid using bare except clauses like below codes
try:
	linux_interaction()
	with open('file.log') as file:
		read_data = file.read()
except FileNotFoundError as fnf_error:
	print(fnf_error)
except AssertionError as error:
	print(error)
	print("Linux linux_interaction() function was not executed.")