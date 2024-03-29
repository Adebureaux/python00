import sys

# Part One

cookbook = {}

cookbook['sandwich'] = { 'ingredients': [ 'ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10 }
cookbook['cake'] = { 'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60 }
cookbook['salad'] = { 'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15 }


# Part Two

def print_names():
	names = list(cookbook.keys())
	if names:
		print('Recipe(s) :')
		for name in names:
			print('- ' + name)
	else:
		print('There is no recipe in the cookbook')

def print_details(name):
	recipe = cookbook.get(name)
	if recipe:
		print("Recipe details of '" + name + "' :")
		if len(recipe['ingredients']):
			print(f"Ingredient(s) list: {recipe['ingredients']}")
		if recipe['meal']:
			print(f"To be eaten for {recipe['meal']}")
		print(f"Takes {recipe['prep_time']} minutes of cooking")
	else:
		print("No details available for the recipe '" + name + "'")

def delete_recipe(name):
	if cookbook.get(name):
		del cookbook[name]
		print(f"'{name}' successfully removed")
	else:
		print(f"'{name}' does not exist")

def add_recipe():
	while True:
		name = input('>> Enter a name:\n')
		if name:
				break
	print('>> Enter ingredients:')
	ingredients = []
	while True:
		ingredient = input()
		if ingredient:
				ingredients.append(ingredient)
		else:
				break
	meal = input('>> Enter meal type:\n')
	while True:
		try:
			prep_time = int(input('>> Enter a preparation time:\n'))
			if prep_time >= 0:
				break
			else:
				print('You should type a positive number')
		except ValueError:
				print('You should type a number')
	new_recipe = { 'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time }
	cookbook[name] = new_recipe


# Part Three

def print_usage():
		print('List of available option:')
		print('\t1: Add a recipe')
		print('\t2: Delete a recipe')
		print('\t3: Print a recipe')
		print('\t4: Print the cookbook')
		print('\t5: Quit\n')

def _add():
	print('Adding a new recipe')
	add_recipe()
	print('Recipe successfully added !')

def _delete():
	name = input('Please type a recipe name\n>> ')
	delete_recipe(name)

def _print_recipe():
	name = input('Please type a recipe name\n>> ')
	print_details(name)

def _print_cookbook():
	print_names()

def _quit():
	print('Cookbook closed. Goodbye !')

if __name__ == '__main__':
	print('Welcome to the Python Cookbook !')
	print_usage()
	fct = [ _add, _delete, _print_recipe, _print_cookbook, _quit ]
	while True:
		option = input('\nPlease select an option\n>>> ')
		if not option.isdigit() or option < '1' or option > '5':
			print_usage()
			continue
		print()
		fct[int(option) - 1]()
		if option == '5':
			break


