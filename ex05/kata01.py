import sys

# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

if type(kata) is dict:
	for s in kata:
		print(s, kata[s], sep=" was created by ")
else:
	eprint("kata is not a dictionary")
