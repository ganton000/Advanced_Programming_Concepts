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

	# makes f read-only
	f.flags.writeable = False