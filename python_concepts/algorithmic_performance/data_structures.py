from typing import List
from collections import defaultdict, Counter
from time import perf_counter_ns
from random import randint, choice
from string import ascii_uppercase
from patricia import trie
import heapq

def counter_dict(items):
	counter = {}
	for item in items:
		if item not in counter:
			counter[item] = 1
		else:
			counter[item] += 1

	return counter

def counter_defaultdict(items):
	''' each new key is auto assigned a default value (in this case assigned 0)'''
	counter = defaultdict(int)
	for item in items:
		counter[item] += 1
	return counter

def search_word_with_comprehensions(document, word):
	''' O(N) query time '''
	return [ doc for doc in document if word in doc ]

def preprocess(document):
	'''
	preprocess documents to decrease query time;
	query involves simple dictionary lookup (via inverted index search)
	The preprocessing is expensive! And every query requires encoding.
	'''

	index = {}
	for i, doc in enumerate(document):
		for word in doc.split():
			if word not in index:
				index[word] = [i]
			else:
				index[word].append(i)
	return index

def preprocess_with_sets(document):

	index = {}
	for i, doc in enumerate(document):
		for word in doc.split():
			if word not in index:
				index[word] = {i}
			else:
				index[word].add(i)
	return index

def query_word_with_inverted_index(preprocessed_doc_index, document, word):
	''' associates each word with list of documents where the word is present (by the index) '''

	result_docs = [ document[i] for i in preprocessed_doc_index[word] ]
	return result_docs

def query_words_with_inverted_index_set(preprocessed_doc_index, document, word1, word2):
	result_docs = [ document[i] for i in preprocessed_doc_index[word1].intersection(preprocessed_doc_index[word2]) ]
	return result_docs

def heapify_collection(collection: list):
	print("Collection: ", collection)

	heapq.heapify(collection)
	print("Heaped Collection: ", collection)

	heapq.heappop(collection) # O(log(N))

	print(collection)
	heapq.heappush(collection, 1)
	print(collection)

def generate_unique_random_strings(length: int) -> str:

	return ''.join(choice(ascii_uppercase) for i in range(length))


def get_trie(string_arr: List[str]):

	strings_dict = { s:0 for s in string_arr }

	# dict where all values are 0
	strings_trie = trie(**strings_dict)

	return strings_trie

def find_longest_prefix_with_trie(strings_trie: dict, prefix: str):

	return list(strings_trie.iter(prefix))

if __name__ == "__main__":

	items = [ randint(0,100) for _ in range(100) ]

	start_time = perf_counter_ns()
	counter_res = counter_dict(items) # most efficient for small N
	tot_time = perf_counter_ns() - start_time
	print(f"total time (dict): {tot_time} nanoseconds\n")

	start_time = perf_counter_ns()
	counter_res = counter_defaultdict(items)
	tot_time = perf_counter_ns() - start_time
	print(f"total time (collections.defaultdict): {tot_time} nanoseconds\n")

	start_time = perf_counter_ns()
	counter_res = Counter(items) # most efficient for large N
	tot_time = perf_counter_ns() - start_time
	print(f"total time (collections.Counter): {tot_time} nanoseconds\n")

	docs = [
		"the cat is under the table",
		"the dog is under the table",
		"cats and dogs smell roses",
		"Carla eats an apple"
	]

	word = "table"
	start_time = perf_counter_ns()
	search_word_with_comprehensions(docs, word)
	tot_time = perf_counter_ns() - start_time
	print(f"total time (list comprehension): {tot_time} nanoseconds\n")

	preprocessed_doc_index = preprocess(docs)
	start_time = perf_counter_ns()
	results = query_word_with_inverted_index(preprocessed_doc_index, docs, word)
	print(results)
	tot_time = perf_counter_ns() - start_time
	print(f"total time (inverted index): {tot_time} nanoseconds\n")

	preprocessed_doc_index = preprocess_with_sets(docs)
	start_time = perf_counter_ns()
	results = query_words_with_inverted_index_set(preprocessed_doc_index, docs, word, "cat")
	print(results)
	tot_time = perf_counter_ns() - start_time
	print(f"total time (inverted index): {tot_time} nanoseconds\n")

	collection = [10, 3, 3, 4, 5, 6]
	result = heapify_collection(collection)
	print(result)
	print("")

	strings_arr = [ generate_unique_random_strings(32) for i in range(10000) ]
	prefix = "AA"

	start_time = perf_counter_ns()
	matches = [ s for s in strings_arr if s.startswith(prefix) ]
	startswith_time = perf_counter_ns() - start_time
	print(f"total time for prefix lookup (with str.startswith): {startswith_time} nanoseconds\n")
	print(matches)
	print(len(matches))

	strings_trie = get_trie(strings_arr)
	start_time = perf_counter_ns()
	matches = find_longest_prefix_with_trie(strings_trie, prefix)
	trie_time = perf_counter_ns() - start_time
	print(f"total time for prefix lookup (with patricia.trie): {trie_time} nanoseconds\n")
	print(matches)
	print(len(matches))

	assert trie_time < startswith_time, f"str.startswith is faster by {trie_time - startswith_time} nanonseconds"
