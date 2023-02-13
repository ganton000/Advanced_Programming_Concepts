from queue import Queue
from threading import Thread


class ClosableQueue(Queue):

	SENTINEL = object()

	def close(self):
		self.put(self.SENTINEL)

	def __iter__(self):
		while True:
			item = self.get()
			try:
				if item is self.SENTINEL:
					return
				yield item
			finally:
				self.task_done()

class StoppableWorker(Thread):

	def __init__(self, func, in_queue, out_queue):
		super().__init__()
		self.func = func
		self.in_queue = in_queue
		self.out_queue = out_queue

	def run(self):
		# in_queue will eventually get exhausted at SENTINEL
		for item in self.in_queue:
			result = self.func(item)
			self.out_queue.put(item)

def download(item):
	return item

def resize(item):
	return item

def upload(item):
	return item

if __name__ == "__main__":

	buffer_size = 10

	download_queue = ClosableQueue(buffer_size)
	resize_queue = ClosableQueue(buffer_size)
	upload_queue = ClosableQueue(buffer_size)

	done_queue = ClosableQueue()

	threads = [
		StoppableWorker(download, download_queue, resize_queue),
		StoppableWorker(resize, resize_queue, upload_queue),
		StoppableWorker(upload, upload_queue, done_queue)
	]

	for thread in threads:
		thread.start()

	for _ in range(1000):
		download_queue.put(object())

	download_queue.close()
	print("All objects in download queue have been added")
	download_queue.join()
	print("Wait until task_done is called on every item pulled from download_queue")

	resize_queue.close()
	print("All objects in resize queue have been added")
	resize_queue.join()
	print("Wait until task_done is called on every item pulled from resize_queue")

	upload_queue.close()
	print("All objects in upload queue have been added")
	upload_queue.join()
	print("Wait until task_done is called on every item pulled from upload_queue")

	print(done_queue.qsize(), "items finished")

	for thread in threads:
		thread.join()