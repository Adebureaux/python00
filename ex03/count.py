import sys
import string

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def count_punctuation(s):
	count = 0
	for i in range(0, len(s)):
		if s[i] in string.punctuation:  
			count = count + 1
	return count

def text_analyzer(s):
	'''Takes a string and print number of: characters, uppercase letters, lowercase letters, punctuation marks, spaces'''
	if not s:
		print("nothing provided, please provide a string")
	elif not isinstance(s, str):
		eprint("error: argument is not a string")
	else:
		print(f"The text contains {len(s)} character(s):")
		print(f"- {sum(map(str.isupper, s))} upper letter(s)")
		print(f"- {sum(map(str.islower, s))} lower letter(s)")
		print(f"- {count_punctuation(s)} punctuation mark(s)")
		print(f"- {s.count(' ')} space(s)")


if __name__ == "__main__":
	if len(sys.argv) > 2:
		eprint("error: more than one argument are provided")
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		text_analyzer('')
