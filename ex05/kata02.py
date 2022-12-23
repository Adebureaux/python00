import sys

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def f_isdigit(n, digits):
	'''Takes a variable to verify if it's an integer, optionally takes an int to define how much digits are expected'''
	try:
		int(n)
	except ValueError:
		return False
	if len(str(n)) > digits:
		return False
	return True

def fill_zero(n, digits):
	l = digits - len(str(n))
	return str(l*"0"+str(n))

if type(kata) is tuple:
	if len(kata) is not 5:
		eprint("error: kata lenght must be 5")
	elif f_isdigit(kata[0], 4) and f_isdigit(kata[1], 2) and f_isdigit(kata[2], 2) and f_isdigit(kata[3], 2) and f_isdigit(kata[4], 2):
		print(f"{fill_zero(kata[1], 2)}/{fill_zero(kata[2], 2)}/{fill_zero(kata[0], 4)} {fill_zero(kata[3], 2)}:{fill_zero(kata[4], 2)}")
	else:
		eprint("error: kata format is not valid")
else:
	eprint("error: kata is not a tuple")
