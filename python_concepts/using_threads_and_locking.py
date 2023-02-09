import threading


class Counter(object):

	def __init__(self):
		self.count = 0

	def increment(self, offset):
		self.count += offset

def worker(sensor_index, how_many, counter):
	for _ in range(how_many):
		# Do the sensor readings
		counter.increment(1)


if __name__ == "__main__":

	worker_count = 5
	barrier = threading.Barrier(worker_count)

	threads = []
	how_many = 10000
	counter = Counter()
	for i in range(worker_count):
		args = (i, how_many, counter)
		thread = threading.Thread(target=worker, args=args)
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()

print(counter.count)
