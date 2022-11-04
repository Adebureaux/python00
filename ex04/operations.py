import sys

def sum(a, b):
	return a + b

if len(sys.argv) == 1:
	print("Usage: python operations.py <number1> <number2>")
elif len(sys.argv) != 3:
	sys.stderr.write("AssertionError: too many arguments")
else:
	print("Sum: ")
# Sum: A+B
# Difference: A-B
# Product: A*B
# Quotient: A/B
# Remainder: A%B
