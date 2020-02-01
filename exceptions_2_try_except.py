def linux_interaction():
	assert ('linux' in sys.platform), "Function can only run in linux."
	print('Doing something')

# test 1
# try:
#	linux_interaction()
# except:
#	pass # return blank but program did not crash

# test 2
# try:
#	linux_interaction()
# except: # you did not get to see was the type of error
#	print('Linux function was not executed') 

# test 3
try:
	linux_interaction()
except AssertionError as error:
	print(error)
	print('Linux function was not executed') 