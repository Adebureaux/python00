import sys

# Put this at the top of your kata04.py file
kata = (0, 4, 132.422222, 10000, 12345.67)

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def is_nninteger(n, digit):
	'''Takes a variable to verify if it's a non-negative integer, optionally takes an int to define how much digits are expected'''
	try:
		t = int(n)
	except ValueError:
		return False
	if len(str(n)) > digit or t < 0:
		return False
	return True

def is_type(n, fn):
	'''Takes a variable to verify if it's an integer'''
	try:
		fn(n)
	except ValueError:
		return False
	return True

def fill_zero(n, digits):
	l = digits - len(str(n))
	return str(l*"0"+str(n))

if type(kata) is tuple:
	if len(kata) != 5:
		eprint("error: kata lenght must be 5")
	elif is_nninteger(kata[0], 2) and is_nninteger(kata[1], 2) and is_type(kata[2], float) and is_type(kata[3], int) and is_type(kata[4], float):
		print(f"module_{fill_zero(kata[0], 2)}, ex_{fill_zero(kata[1], 2)} : {format(kata[2], '.2f')}, {kata[3]:.2e}, {kata[4]:.2e}")
	else:
		eprint("error: kata format is not valid")
else:
	eprint("error: kata is not a tuple")
