import sys

def reverse_string(str):
	return str[::-1]

result = ""

for i in range(1, len(sys.argv)):
	if i > 1:
		result += " "
	result += sys.argv[i].swapcase()

if len(sys.argv) > 1:
	print(reverse_string(result))
