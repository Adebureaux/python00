import sys

# Put this at the top of your kata00.py file
kata = (100, 312, "210", "145")

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def f_isdigit(n):
	'''Takes a variable to verify if it's a digit, optionally takes an int to define how much digits are expected'''
	try:
		int(n)
		return True
	except ValueError:
		return False

if type(kata) is tuple:
	for digit in kata:
		if f_isdigit(digit) is False:
			sys.exit("error: kata must be filled with digits")
	print(f"The {len(kata)} numbers are: ", end="")
	print(*kata, sep=", ")
else:
	eprint("error: kata is not a tuple")
