
def log(message, *values):
	if not values:
		print(message)
	else:
		values_str = ", ".join(str(x) for x in values)
		print("%s: %s" %(message, values_str))

log("My numbers are", [1,2])
log("My numbers 2")

favorites = [7, 13, 33, 99]
log('My favorite numbers', *favorites)

def my_generator():
	for i in range(10):
		yield i

log('Hi there', *my_generator())
# Above doesn't pass in a generator but a tuple, which is a problem!