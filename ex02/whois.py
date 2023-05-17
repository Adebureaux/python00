import sys

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def is_integer(str):
	'''Takes a variable to verify if it's an integer'''
	try:
			int(str)
	except ValueError:
			return False
	return True

if len(sys.argv) > 1:
	if len(sys.argv) != 2:
		eprint("error: more than one argument are provided")
	elif not is_integer(sys.argv[1]):
		eprint("error: argument is not an integer")
	else:
		n = int(sys.argv[1])
		if not n:
			print("I'm Zero")
		elif n % 2:
			print("I'm Odd")
		else:
			print("I'm Even")
