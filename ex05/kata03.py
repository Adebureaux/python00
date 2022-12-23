import sys

# Put this at the top of your kata03.py file
kata = "The right format"

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

if type(kata) is str:
	len = len(kata)
	if len <= 42:
		for i in range(len, 42):
			print('-', end='')
		print(kata, end='')
	else:
		eprint("error: string lenght is higher than 42")
else:
	eprint("error: kata is not a string")
