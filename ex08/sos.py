import sys

mapping = {
		'A': '.-',
		'B': '-...',
		'C': '-.-.',
		'D': '-..',
		'E': '.',
		'F': '..-.',
		'G': '--.',
		'H': '....',
		'I': '..',
		'J': '.---',
		'K': '-.-',
		'L': '.-..',
		'M': '--',
		'N': '-.',
		'O': '---',
		'P': '.--.',
		'Q': '--.-',
		'R': '.-.',
		'S': '...',
		'T': '-',
		'U': '..-',
		'V': '...-',
		'W': '.--',
		'X': '-..-',
		'Y': '-.--',
		'Z': '--..',
		'1': '.----',
		'2': '..---',
		'3': '...--',
		'4': '....-',
		'5': '.....',
		'6': '-....',
		'7': '--...',
		'8': '---..',
		'9': '----.',
		'0': '-----',
}

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)
	sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		eprint('ERROR: Program must take one or more arguments')
	joined = " ".join(sys.argv[1:]).upper()
	if not all(w.isalnum() or w.isspace() for w in joined):
		eprint('ERROR: Argument(s) must contain only alphanumeric character(s) or space(s)')
	splited = joined.split()
	for i, w in enumerate(splited):
		for index, c in enumerate(w):
			print(mapping[c], end=" " if index != len(w) - 1 or i != len(splited) - 1 else "")
		if i != len(splited) - 1:
			print('/', end=" ")
		else:
			print()

