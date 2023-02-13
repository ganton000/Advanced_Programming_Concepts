import json
import logging
from random import randint
from contextlib import contextmanager

def slicing_concepts():

	a = [1,2,3,4,5,6,7,8,9]
	b = a[:]

	try:
		assert id(a) == id(b) # python3 -O main.py ( -O flag does not throw assertion!)
	except AssertionError:
		print("assigning a[:] to another variable makes a copy of a")

	assert a == b
	assert a is not b
	assert id(a) != id(b)

	odd_elements = a[::2]
	even_elements = a[1::2]
	print(odd_elements)
	print(even_elements)
	print("")

def create_random_bits():

	random_bits = 0

	for i in range(64):
		if randint(0,1):
			random_bits |= 1 << i

	print(bin(random_bits))
	print("")

def enumerate_lists():

	flavor_list = ["vanilla", "chocolate", "pistachio", "strawberry"]
	for i, flavor in enumerate(flavor_list):
		print("%d: %s" %(i+1, flavor))

	print ("")

	for i, flavor in enumerate(flavor_list, 1):
		print("%d: %s" %(i, flavor))

	print("")

def for_else_concept(a=4, b=9):

	for i in range(2, min(a,b)+1):
		print('Testing', i)
		if (a % i == 0) and (b % i == 0):
			print("Not coprime\n")
			break
	else: #else only runs when total range is exhausted
		print("Coprime\n")

UNDEFINED = object()
def try_except_else_finally_clauses(path: str):

	handle = open(path, 'r+') # IOError
	try:
		data = handle.read() # UnicodeDecode Error
		op = json.loads(data) # ValueError
		value = op["numerator"] / op["denominator"] # ZeroDivisionError
	except ZeroDivisionError:
		return UNDEFINED
	else:
		op["result"] = value
		result = json.dumps(op)
		handle.seek(0)
		handle.write(result) # IOError
		return value
	finally:
		handle.close() # Always runs

@contextmanager
def debug_logging(level):
	logger = logging.getLogger()
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	# when using debug_logging with 'with' statement
	# the code in the 'with' block will run on yield
	# so everything before try is general set-up
	# and when 'with' block exits, the finally executes
	try:
		yield
	finally:
		logger.setLevel(old_level)

# initialize logger level to WARNING
logging.getLogger().setLevel(logging.WARNING)

def logging_function():
	logging.debug("Some debug info")
	logging.error("A real error!")
	logging.debug("More debugging!")
	logging.info("Info block")

@contextmanager
def swallow_exception(cls):
	try:
		yield
	except cls:
		logging.exception("Swallowing exception")

def swallowed_exception_example():
	value = 20
	with swallow_exception(ZeroDivisionError):
		value /= 0
	print("Done!")

@contextmanager
def log_level(level, name):
	logger = logging.getLogger(name)
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield logger
	finally:
		logger.setLevel(old_level)

if __name__ == "__main__":
	slicing_concepts()
	create_random_bits()
	enumerate_lists()
	for_else_concept()

	tmp_path = '/tmp/random_data.json'
	with open(tmp_path, 'w') as handle:
		handle.write('{"numerator": 100, "denominator": 10}')

	result = try_except_else_finally_clauses(tmp_path)
	print(result is UNDEFINED)
	print("result: ", result)

	print("\nLog level configured to WARNING")
	logging_function()

	print("\nContextManager set log level to DEBUG")
	with debug_logging(logging.DEBUG):
		logging_function()

	print("\nContextManager set log level to INFO")
	with debug_logging(logging.INFO):
		logging_function()

	print("\nCatching exceptions in contextmanager")
	swallowed_exception_example()

	print("\nOverriding the global logger with contextmanager")
	with log_level(logging.DEBUG, 'my-log') as logger:
		logging.debug('This is the global logger and will not show')
		logger.debug('This is the my-log logger!')

	logging.error('Global logger')

