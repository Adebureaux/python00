import sys

# Put this at the top of your kata00.py file
kata = (100, 312, 210, 145)

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def is_integer(str):
	'''Takes a variable to verify if it's an integer'''
	try:
			int(str)
	except ValueError:
			return False
	return True

if type(kata) is tuple:
	for digit in kata:
		if is_integer(digit) is False:
			sys.exit("error: kata must be filled with digits")
	print(f"The {len(kata)} numbers are: ", end="")
	print(*kata, sep=", ")
else:
	eprint("error: kata is not a tuple")
