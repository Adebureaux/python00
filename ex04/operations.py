import sys

def is_integer(str):
	'''Takes a variable to verify if it's an integer'''
	try:
			int(str)
	except ValueError:
			return False
	return True

if len(sys.argv) == 1:
	print("Usage: python operations.py <number1> <number2>")
elif len(sys.argv) != 3:
	sys.stderr.write("Error: wrong number of arguments\n")
else:
	for arg in sys.argv[1:]:
		if not is_integer(arg):
			sys.exit("Error: arguments must be integers")
	numbers = [int(arg) for arg in sys.argv[1:]]
	print(f"Sum:		{sum(numbers)}")
	print(f"Difference:	{numbers[0] - numbers[1]}")
	print(f"Product:	{numbers[0] * numbers[1]}")
	if numbers[1] != 0:
		print(f"Quotient:	{numbers[0] / numbers[1]}")
		print(f"Remainder:	{numbers[0] % numbers[1]}")
	else:
		print(f"Quotient:	ERROR (division by zero)")
		print(f"Remainder:	ERROR (modulo by zero)")
