# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for s in kata:
	print(s, kata[s], sep=" was created by ")
