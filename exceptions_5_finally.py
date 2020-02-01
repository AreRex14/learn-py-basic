def linux_interaction():
	assert ('linux' in sys.platform), "Function can only run in linux."
	print('Doing something')

try:
	linux_interaction()
except AssertionError as error:
	print(error)
else: # no exception, run else code and with extra handling of other exceptions more
	try:
		with open('file.log') as file:
			read_data = file.read()
	except FileNotFoundError as fnf_error:
		print(fnf_error)
finally:
	print('Cleaning up, irrespective of any exceptions.')