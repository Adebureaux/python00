# Part One

cookbook = {}

cookbook['Sandwich'] = { 'ingredients': [ 'ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10 }
cookbook['Cake'] = { 'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60 }
cookbook['Salad'] = { 'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15 }


# Part Two

def print_names():
	names = list(cookbook.keys())
	print('Recipe names :')
	for name in names:
		print(name)

def print_details():
	print()

print_names()
