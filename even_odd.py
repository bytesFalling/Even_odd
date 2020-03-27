import string


def main():

	print "Even odd program"
	even_odd()


def even_odd():
	try:
		user_input = int (input ( "Enter integer number: " ))
		if ( user_input%2 == 0):
			print "It's even number"
		else:
			print "It's odd number"
		if ( user_input == 'yes'):
			main()
	except:
		print "Unexpect error happend. Starting program over"
		main()

main()
