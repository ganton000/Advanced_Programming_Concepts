import os
import random
from threading import Thread
from tempfile import TemporaryDirectory


class InputData(object):

	def read(self):
		raise NotImplementedError

class PathInputData(InputData):
	'''Polymorphism of read interface'''
	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		with open(self.path, 'rb') as handle:
			return handle.read()

class Worker(object):

	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementedError

	def reduce(self):
		raise NotImplementedError

class LineCountWorker(Worker):

	def map(self):
		data = self.input_data.read()

		#counts how often newline char occuers
		self.result = data.count(b'\n')

	def reduce(self, other):
		''' takes two worker instances and combines into one '''

		self.result += other.result

def generate_inputs(data_dir):
	## creates path to data file based on every file in directory
	for name in os.listdir(data_dir):
		yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
	workers = []

	for input_data in input_list:
		workers.append(LineCountWorker(input_data))

	return workers

def execute(workers):
	threads = [Thread(target=w.map) for w in workers]

	for thread in threads: thread.start()
	for thread in threads: thread.join() # waits for threads to finish

	first, rest_of_workers = workers[0], workers[1:]

	for worker in rest_of_workers:
		# final result sits in first worker's result
		first.reduce(worker)

	return first.result

def mapreduce(data_dir):
	inputs = generate_inputs(data_dir)
	workers = create_workers(inputs)
	return execute(workers)

def write_test_files(tmpdir):
	''' creates 100 test files with random data '''
	for i in range(100):
		with open(os.path.join(tmpdir, str(i)), "w") as handle:
			handle.write("\n" * random.randint(0,100))


if __name__ == "__main__":

	with TemporaryDirectory() as tmpdir:
		write_test_files(tmpdir)
		result = mapreduce(tmpdir)
		print(result)