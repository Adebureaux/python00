import sys

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

if len(sys.argv) > 1:
	if sys.argv[1][0] == '-':
		sys.argv[1] = sys.argv[1][1:]
	if len(sys.argv) != 2:
		eprint("error: more than one argument are provided")
	elif not sys.argv[1].isdigit():
		eprint("error: argument is not an integer")
	else:
		n = int(sys.argv[1])
		if not n:
			print("I'm Zero")
		elif n % 2:
			print("I'm Odd")
		else:
			print("I'm Even")
