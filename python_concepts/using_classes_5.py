
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

if __name__ == "__main__":
	pass