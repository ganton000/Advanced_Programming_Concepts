'''
Due to GIL (global interpretor lock) sets it so only one python thread runs at a given time
'''
import time
import threading
import select

def factorize(number):
	for i in range(1, number+1):
		if number % i == 0:
			yield i

class FactorizeThread(threading.Thread):

	def __init__(self, number):
		super().__init__()
		self.number = number

	def run(self):
		self.factor = factorize(self.number)

def slow_systemcall():
	select.select([], [], [], 0.1) # simulate slow i/o call



if __name__ == "__main__":

	numbers = [20202094858092, 5958059594830, 304959589482, 40484843039]

	start = time.time()
	for num in numbers:
		factorize(numbers)

	tot_time = time.time() - start
	print(f"Time to factorize took: {tot_time}")

	start = time.time()
	threads = []
	for num in numbers:
		thread = FactorizeThread(num)
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()

	tot_time = time.time() - start
	print(f"Time to factorize (with threads) took: {tot_time}")
	print("")


	print("I/O Example: ")

	start = time.time()
	for _ in range(5):
		slow_systemcall()

	tot_time = time.time() - start
	print(f"Time to run slow system i/o call took: {tot_time}")
	print("")

	start = time.time()

	threads = []
	for _ in range(5):
		thread = threading.Thread(target=slow_systemcall)
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()

	tot_time = time.time() - start
	print(f"Time to run slow system i/o call (with threading) took: {tot_time}")
	print("")

	start = time.time()

	threads = []
	for _ in range(5):
		thread = threading.Thread(target=slow_systemcall)
		thread.start()
		threads.append(thread)

	def compute_location(index):
		# some basic work in main thread
		pass

	for i in range(5):
		compute_location(i)

	for thread in threads:
		thread.join()

	tot_time = time.time() - start
	print(f"Time to run slow system i/o call (with threading and function in main thread) took: {tot_time}")


'''
The compute time operations with the numbers didn't occur in parallel
Because behind the scene, the CPU time is split between the different threads
Therefore, threading had no performance benefit for CPU heavy computations.

The benefits occur for independent tasks, generally I/O intensive tasks.
'''