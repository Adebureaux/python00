import sys
import string

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)
	sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		eprint('ERROR: Wrong number of argument')
	try:
		n = int(sys.argv[2])
		if n <= 0:
			eprint('ERROR: Second argument must be a positive integer')
	except ValueError:
			eprint('ERROR: Second argument must be an integer')
	s = sys.argv[1].translate(str.maketrans('', '', string.punctuation)).split()
	dst = [w for w in s if len(w) > n]
	print(dst)
