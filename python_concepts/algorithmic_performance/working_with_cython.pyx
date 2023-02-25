
def hello():
	print("Hello world!")

cdef simple_loop():

	cdef int i,j = 0

	for i in range(100):
		j +=1
	return j

cdef casting_example():

	cdef double b
	cdef int a = 0
	b = <double> a #casts a to double


## below is still python function that switches back to interpreter
def max_python(int a, int b):
	return a if a > b else b

## cython function -- optimized by interpreter since translated to C
cdef int max_cython(int a, int b):
	return a if a > b else b

## callable from Python and translatable to performant C
## generates a version for each language
cpdef int max_hybrid(int a, int b):
	return a if a > b else b

if __name__ == "__main__":
	hello()
	result = simple_loop()
	print(result)