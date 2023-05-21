from time import sleep, time

def ft_progress(lst):
	total = len(lst)
	bar_length = 20
	start_time = time()
	max_num_len = len(str(total))
	for i, item in enumerate(lst, 1):
		progress = i / total
		completed = int(progress * bar_length)
		remaining = bar_length - completed
		bar = "[" + "=" * completed + ">" + "-" * remaining + "]"
		percentage = int(progress * 100)
		elapsed_time = time() - start_time
		eta = (elapsed_time / progress) - elapsed_time if progress > 0 else 0
		progress_str = f"{i:>{max_num_len}}/{total}"
		print(f"ETA: {eta:.2f}s [{percentage:3}%]{bar} {progress_str} | elapsed time {elapsed_time:.2f}s", end="\r")
		yield item
	return total

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
	# print()
	# print(ret)