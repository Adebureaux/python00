import sys

# def plus(a, b):
# 	numbers = [int(arg) for arg in sys.argv[1:]]
# 	sum = sum(numbers)
# 	return sum(a + b)

def isdigit(s):
    try:
        int(s)
        return True
    except ValueError:
    	return False

if len(sys.argv) == 1:
	print("Usage: python operations.py <number1> <number2>")
elif len(sys.argv) != 3:
	sys.stderr.write("Error: too many arguments\n")
else:
	for arg in sys.argv[1:]:
		if not isdigit(arg):
			sys.exit("Error: arguments must be integers")
	numbers = [int(arg) for arg in sys.argv[1:]]
	print(f"Sum:		{sum(numbers)}")
	print(f"Difference:	{numbers[0] - numbers[1]}")
	print(f"Product:	{numbers[0] * numbers[1]}")
	if numbers[1] is not 0:
		print(f"Quotient:	{numbers[0] / numbers[1]}")
		print(f"Remainder:	{numbers[0] % numbers[1]}")
	else:
		print(f"Quotient:	ERROR (division by zero)")
		print(f"Remainder:	ERROR (modulo by zero)")
