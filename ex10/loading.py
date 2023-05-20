# from tqdm import tqdm
import time

# for i in tqdm(range(100)):
#	 time.sleep(0.1)

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
				# ...

				yield

		print()	# Print a new line at the end

# Example usage
my_list = [1, 2, 3, 4, 5]

for _ in ft_progress(my_list):
		time.sleep(0.1)
		# Do additional processing or display here
		pass