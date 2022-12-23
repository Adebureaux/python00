import sys

# Put this at the top of your kata04.py file
kata = (0, 4, 132.422222, 10000, 12345.67)

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def f_isnndigit(n, digit):
	'''Takes a variable to verify if it's a non-negative integer, optionally takes an int to define how much digits are expected'''
	try:
		int(n)
	except ValueError:
		return False
	if len(str(n)) > digit or n < 0:
		return False
	return True

def isdigit(n):
	'''Takes a variable to verify if it's an integer'''
	try:
		int(n)
	except ValueError:
		return False
	return True

def isdecimal(n):
	'''Takes a variable to verify if it's a decimal'''
	try:
		float(n)
	except ValueError:
		return False
	return True

def fill_zero(n, digits):
	l = digits - len(str(n))
	return str(l*"0"+str(n))

if type(kata) is tuple:
	if len(kata) is not 5:
		eprint("error: kata lenght must be 5")
	elif f_isnndigit(kata[0], 2) and f_isnndigit(kata[1], 2) and isdecimal(kata[2]) and isdigit(kata[3]) and isdecimal(kata[4]):
		print(f"module_{fill_zero(kata[0], 2)}, ex_{fill_zero(kata[1], 2)} : {format(kata[2], '.2f')}, {float(format(kata[3], '2f')):e}, {kata[4]:e}")
	else:
		eprint("error: kata format is not valid")
else:
	eprint("error: kata is not a tuple")
