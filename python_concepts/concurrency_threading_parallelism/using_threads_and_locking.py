import threading


class Counter(object):

	def __init__(self):
		self.count = 0
		self.lock = threading.Lock()

	def increment(self, offset):
		with self.lock:
			self.count += offset
		'''
		above line of code is equivalent to the bottom 3 lines
		So with multi-threading without locks, execution can be suspended in between any of these 3 lines, altering expected results.
		'''
		#value = getattr(self, "count")
		#result = value + offset
		#setattr(self, "count", result)

def worker(sensor_index, how_many, counter):
	barrier.wait()
	for _ in range(how_many):
		# Do the sensor readings
		counter.increment(1)


if __name__ == "__main__":

	worker_count = 5
	barrier = threading.Barrier(worker_count)

	threads = []
	how_many = 1000000
	counter = Counter()
	for i in range(worker_count):
		args = (i, how_many, counter)
		thread = threading.Thread(target=worker, args=args)
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()

print(counter.count)
