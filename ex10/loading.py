import time

def ft_progress(lst):
		total = len(lst)
		bar_length = 30

		for i, item in enumerate(lst):
				progress = (i + 1) / total
				completed = int(progress * bar_length)
				remaining = bar_length - completed
				bar = "[" + "#" * completed + "-" * remaining + "]"
				percentage = int(progress * 100)

				print(f"Progress: {bar} {percentage}%", end="\r")

				# Process the current item

				yield

		print()

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += 1
	time.sleep(0.01)
print()
print(ret)