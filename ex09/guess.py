from random import randint

if __name__ == '__main__':
	print('This is an interactive guessing game!')
	print('You have to enter a number between 1 and 99 to find out the secret number.')
	print("Type 'exit' to end the game.")
	print('Good luck!\n')
	find = randint(1, 99) 
	attempt = 0

	while True:
		attempt += 1
		inpt = input('What is your guess between 1 and 99 ?\n>> ')
		if inpt == 'exit':
			break
		try:
			n = int(inpt)
			if n < 1 or n > 99:
				print('Input Error: You should type a number beteween 1 and 99.')
				continue
		except ValueError:
				print('Input Error: You should type a number beteween 1 and 99.')
				continue
		if n == find:
			if find == 42:
				print('As Deep Thought, after seven and a half million years of calculation, the answer finally turns out to be 42.')
			if attempt == 1:
				print('Congratulations! You got it on your first try!')
			else:
				print(f'Congratulations! You found the answer in {attempt} attempts!')
			break
		elif n < find:
			print('Too low !')
		else:
			print('Too high!')