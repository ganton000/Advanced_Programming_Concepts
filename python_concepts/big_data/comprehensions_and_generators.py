import random
from typing import Union

def comprehensions(file_name: str) -> None:
	chile_ranks = {"ghost": 1, "habanero": 2, "cayenne": 3}

	dict_comp = {key:name for key, name in chile_ranks.items()}
	set_comp = {len(name) for name in chile_ranks.keys()}

	print(dict_comp)
	print(set_comp)

	matrix = [[1,2,3],[4,5,6],[7,8,9]]

	double_for_comp = [x for row in matrix for x in row]
	print(double_for_comp)

	matrix_3d = [ [[1,2],[3,4]], [[5,6,],[7,8]], [[9,10],[11,12]]]

	triple_for_comp = [x for matrix_2d in matrix_3d for row in matrix_2d for x in row]
	print(triple_for_comp)

	squared_matrix = [ [x**2 for x in row] for row in matrix]
	print("\nmatrix: ", matrix)
	print("squared matrix: ", squared_matrix)
	print("")

	a = [1,2,3,4,5,6,7,8,9,10]
	b = [x for x in a if x > 4 and x % 2 == 0]
	c = [x for x in a if x > 4 if x % 2 == 0]
	print(b)
	assert b == c

	filtered = [ [x for x in row if x % 3 == 0]
				  for row in matrix if sum(row) >= 10 ]
	print(filtered)
	print("")

	value = [ len(x) for x in open(file_name)]
	print(value)
	print("")

def generator_expressions(file_name: str) -> None:

	it = (len(x) for x in open(file_name))
	print(it)

	roots = ((x, x**0.5) for x in it)
	print(next(roots))
	print(next(roots))
	print(next(roots))
	print(next(roots))

def index_words(text):
	result = []
	if text:
		result.append(0)

	for index, letter in enumerate(text):
		if letter == " ":
			result.append(index + 1)
	return result

address = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."

def index_words_gen(text):
	if text:
		yield 0
	for index, letter in enumerate(text):
		if letter == " ":
			yield index + 1

def index_words_handle(handle):
	offset = 0
	for line in handle:
		if line:
			yield offset
		for letter in line:
			offset += 1
			if letter == " ":
				yield offset

address_lines = '''Four score and seven years ago
our fathers brought forth on this continent
a new nation, conceived in liberty,
and dedicated to the proposition that
all men are created equal.'''

def normalize(numbers: Union[list, iter]) -> list:
	''' iterates over input numbers array twice '''
	''' i.e. sum() and for loop '''
	if iter(numbers) is iter(numbers):
		raise TypeError("Must supply a cointainer")
	numbers = list(numbers)
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100*value/total
		result.append(percent)
	return result

def read_visits(data_path: str) -> iter:
	with open(data_path) as f:
		for line in f:
			yield int(line)

def normalize_iter(get_iter):
	if iter(get_iter) is iter(get_iter):
		raise TypeError("Must supply a cointainer")
	total = sum(get_iter()) # new iterator
	result = []
	for val in get_iter(): # new iter
		percent = 100 * val / total
		result.append(percent)
	return result

class ReadVisits(object):
	def __init__(self, data_path):
		self.data_path = data_path
	def __iter__(self):
		with open(self.data_path) as f:
			for line in f:
				yield int(line)

if __name__ == "__main__":

	file_name = "/tmp/my_file.txt"
	with open(file_name, "w") as f:
		for _ in range(10):
			f.write("a" * random.randint(0,100))
			f.write("\n")

	comprehensions(file_name)
	generator_expressions(file_name)

	result = index_words(address)
	print("\naddress:", address)
	print("Index of words: ", result)

	print("\nResult using generators: ")
	it = index_words_gen(address)
	print(next(it), next(it), next(it), next(it), next(it), "...")

	address_file = "/tmp/address.txt"
	with open(address_file, "w") as f:
		f.write(address_lines)

	with open(address_file) as f:
		it = index_words_handle(f)
		print("\nResult using index_words with file handler:")
		print(next(it), next(it), next(it), next(it), next(it), "...")

	print("")
	number_path = "/tmp/my_numbers.txt"
	with open(number_path, 'w') as f:
		for i in [15,80,35,44,55,100,99,300,2091]:
			f.write('%d\n' % i)

	data = [15,80,35,44,55,100,99,300,2091]
	normalized_data = normalize(data)
	print("Sum: ", sum(normalized_data), "\nNormalized Dataset: ", normalized_data)

	print("\nUsing iterator: ")
	it = read_visits(number_path)
	print(normalize(it))
	print(list(it))

	# Iterators are only exhausted once, so can only use results from them one time!
	# So for functions that read through datasets twice, this can be an issue
	# So should make a copy of iterator

	print("")
	get_iter = lambda: read_visits(number_path)
	result = normalize_iter(get_iter)
	print(result)
	print("")

	'''
	a = [1,2,3]
	for x in a:
		pass

	--> Under the hood:
	it = iter(a)
	it = a.__iter__() # equivalent

	value = next(it)
	value = it.__next__() # equivalent

	So can convert iterator object into class method
	to redefine the __iter__() special method of an object
	'''

	visits = ReadVisits(number_path)
	it = iter(visits)
	it2 = iter(visits)
	it3 = iter(it)
	print("it :::",list(it))
	print("it2 :::",list(it2))
	print("it3 :::",list(it3))
	print(id(it) == id(it2))
	print(id(it) == id(it3))
	'''
	iter() returns the same iterator object twice!
	'''

	result = normalize(visits)
	print(result)

