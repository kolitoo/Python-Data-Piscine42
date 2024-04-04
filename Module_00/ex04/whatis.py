import sys

def main(argv):
	if len(argv) != 2:
		if len(argv) > 2:
			print("AssertionError: more than one argument is provided")
		sys.exit(1)
	try:
		arg = int(argv[1])
	except ValueError:
		print("AssertionError: argument is not an integer")
		sys.exit(1)
	if arg % 2 == 0:
		print("I'm Even.")
	elif arg % 2 != 0:
		print("I'm Odd.")

if __name__ == "__main__":
	main(sys.argv)