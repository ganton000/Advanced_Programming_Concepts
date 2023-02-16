from collections import defaultdict, Counter
from time import perf_counter_ns
from random import randint

def counter_dict(items):
	counter = {}
	for item in items:
		if item not in counter:
			counter[item] = 1
		else:
			counter[item] += 1

	return counter

def counter_defaultdict(items):
	''' each new key is auto assigned a default value (in this case assigned 0)'''
	counter = defaultdict(int)
	for item in items:
		counter[item] += 1
	return counter

if __name__ == "__main__":

	items = [ randint(0,100) for _ in range(100) ]

	start_time = perf_counter_ns()
	counter_res = counter_dict(items) # most efficient for small N
	tot_time = perf_counter_ns() - start_time
	print(f"total time (dict): {tot_time} nanoseconds\n")

	start_time = perf_counter_ns()
	counter_res = counter_defaultdict(items)
	tot_time = perf_counter_ns() - start_time
	print(f"total time (collections.defaultdict): {tot_time} nanoseconds\n")

	start_time = perf_counter_ns()
	counter_res = Counter(items) # most efficient for large N
	tot_time = perf_counter_ns() - start_time
	print(f"total time (collections.Counter): {tot_time} nanoseconds\n")

	docs = [
		"the cat is under the table",
		"the dog is under the table",
		"cats and dogs smell roses",
		"Carla eats an apple"
	]
