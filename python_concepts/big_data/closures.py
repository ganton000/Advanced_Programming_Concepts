from collections import defaultdict

'''
Closures are functions that refer to variables from the scope in which they were defined
'''

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}

class Sorter(object):

	def __init__(self, group):
		self.group = group
		self.found = False

	def __call__(self, x):
		if x in self.group:
			self.found = True
			return (0, x)
		return (1, x)

def sort_priority(numbers, group):
	found = False
	def helper(x):
		nonlocal found
		'''
		group has been closed over to be referred to inside the function
		With assignment, things change and using nonlocal/global may be better option
		'''
		if x in group:
			found = True
			return (0, x)
		return (1,x)

	numbers.sort(key=helper)
	return found

'''
In python, when comparing tuples:
first compare items in index 0 (default order of sort is ascending)
'''
numbers1 = numbers[:]
result = sort_priority(numbers, group)
print(result)
print(numbers)
print("")

'''
Can use classes to not worry about state of variables/closures
'''
sorter = Sorter(group)
print(numbers1)
numbers1.sort(key=sorter)
print(sorter.found)
print(numbers1)
print("")


names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)
print("")

def log_missing():
	print('Key added')
	return 0


d = defaultdict(log_missing)
print(d["foo"])
print(d)
print("")

def increment_with_report(current, increments):
	added_count = 0

	def missing():
		nonlocal added_count
		added_count += 1
		return 0

	result = defaultdict(missing, current)

	for key, offset in increments:
		result[key] += offset

	return result, added_count

current = { "green": 12, "blue": 3}
increments = [("red", 5), ("blue", 17), ("orange", 9)]

print(increment_with_report(current, increments))

class CountMissing(object):
	'''
	class to keep track of state; i.e. stateful object
	is a stateful closure over the added variable

	'''
	def __init__(self) -> None:
		self.added = 0

	def __call__(self):
		''' allows object to be called like a function'''
		self.added += 1
		return 0

counter = CountMissing()
result = defaultdict(counter, current)

for key, offset in increments:
	result[key] += offset

print("")
print(callable(counter))
print(result)
print(counter.added)