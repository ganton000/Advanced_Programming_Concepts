from functools import lru_cache
from joblib import Memory
# the cache is thread safe!
# restrict size of cache to 16 elements with maxsize
# new elements will replace old ones (lru = least recently used)
@lru_cache(maxsize=16)
def sum2(a,b):
	print(f"Calculating {a} + {b}...")
	return a + b

# pip install joblib
# joblib runs similar to lru_cache, except cache results are stored on disk and persist.

memory = Memory("./tmp/")

@memory.cache
def sum3(a,b,c):
	print(f"Calculating {a} + {b} + {c}...")
	return a + b + c

if __name__ == "__main__":

	res = sum2(1,2)
	print(res)
	res = sum2(1,2)
	print(res)
	res = sum2(1,2)

	print(sum2.cache_info()) # examine cache performance
	sum2.cache_clear() # clear cache

	res = sum3(1,2,3)
	print(res)
	res = sum3(1,2,3)
	print(res)
	res = sum3(1,2,3)