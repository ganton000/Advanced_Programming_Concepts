from time import time
from concurrent.futures import (
	ThreadPoolExecutor,
	ProcessPoolExecutor
)


def gcd(pair):
	a, b = pair
	low = min(a,b)
	for i in range(low, 0, -1):
		if a % i == 0 and b % i == 0:
			return i
	return 1

if __name__ == "__main__":
	numbers = [(1963309, 2265973), (2030677, 3814172),
			   (1551643, 2229620), (2039045, 2020802)]


	start = time()
	results = list(map(gcd, numbers))
	total = time() - start
	print(f"Total time with map took {total} seconds")

	os_cpu_count = 4
	pool = ThreadPoolExecutor(max_workers=os_cpu_count)

	start = time()
	results = list(pool.map(gcd, numbers))
	total = time() - start
	print(f"Total time with ThreadPoolExecutor took {total} seconds")

	proc = ProcessPoolExecutor(max_workers=os_cpu_count)
	start = time()
	results = list(proc.map(gcd, numbers))
	total = time() - start
	print(f"Total time with ProcessPoolExecutor took {total} seconds")

'''
How multiprocessing works:

All data in numbers array (input data) is serialized into bytes using pickle module.
Then a new child process is created, separate from main interpreter process.
The pickled data is copied from parent process to child interpreter process over a local socket.
The child interpreter deserializes the data back into python objects using pickle
The child process will then import the python module containing the gcd function, and will run the function on the input data in parallel with other child processes.
Finally, result is serializes back into bytes using Pickle
Will copy those bytes back through same local socket to parent process.
Those bytes will be deserialized into python objects again within the parent process, using pickle
Merges results from multiple children into a single list to return

When to use multiprocessing:

- Functions that don't share state.
- Small amount of data -> Large amounts of computation (aka high leverage functions)
'''