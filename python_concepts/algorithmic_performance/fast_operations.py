import numpy as np
import pandas as pd

if __name__ == "__main__":

	arr = [0,1,2]
	a = np.array(arr)

	print(a.dtype)

	b = np.array(arr, dtype='float32')
	print(b.dtype)
	print("")

	c = np.zeros((3,3))
	print(c)

	d = np.ones((3,3), dtype='float32')
	print(d)

	e = np.empty((3,3))
	print(e)

	f = np.random.rand(3,3)
	print(f)

	print("")

	b = f[0:2,2]
	print(b)
	b[:] = [1,1]
	print(b)

	print(f)
	print("")

	# makes f read-only
	f.flags.writeable = False

	# fancy indexing
	g = np.array([9,8,7,6,5,4,3,2,1,0])
	idx = np.array([0,2,3])

	print(g[idx])
	print(g[[0,2,3]]) # equivalent
	## using tuples will interpret as indexing on multiple dimensions

	h = np.array([
		[0,1,2],
		[3,4,5],
		[6,7,8],
		[9,10,11]
	])

	idx1 = np.array([0,1])
	idx2 = np.array([2,2])
	print("")

	# extract (0,2) and (1,2) elements
	print(h[idx1, idx2])
	print("")

	# can extract with multi-dimensional arrays

	idx3 = [[0,1], [3,2]]
	idx4 = [[0,2], [1,1]]
	print(h[idx3, idx4])
	print("")

	# bool masking
	j = np.array([0,1,2,3,4,5,6,7])

	bool_mask = np.array([True, False, False, False, False, False, True, True])

	print(j[bool_mask])

	print("")


	result = np.take(h, [0, 2], axis=0)
	print(result)
	print("")


	## Broadcasting

	A = np.array([[1, 2], [3, 4]])
	B = np.array([[5, 6], [7, 8]])

	C = A*B
	print(C) #element-wise multiplication

