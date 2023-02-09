from queue import Queue
from threading import Thread
import time

buffer_size = 1
queue = Queue(buffer_size)


def consumer():
	print("Consumer waiting")

	time.sleep(0.1)

	queue.get()
	print("Consumer got 1")
	queue.get() # blocks consumer until object is put into queue
	print("Consumer got 2")

	print("Consumer done")

def consumer2():
	print("Consumer waiting")

	queue.get()
	print("Consumer working")

	#do some work
	print("Consumer done")
	queue.task_done()

if __name__ == "__main__":

	thread = Thread(target=consumer)
	thread.start()


	print("Producer putting objects")

	queue.put(object())
	print("Producer put 1")
	queue.put(object())
	print("Product put 2")
	thread.join()

	print("Producer done")
	print("")

	thread = Thread(target=consumer2)
	thread.start()

	queue.put(object())
	print("Producer is waiting")
	#queue.join()
	print("Producer is done")


'''
Some issues/comments:

- Producer can input into queue faster than consumer can get
- Soln: Define a buffer size (maximum amount of pending work allowed between phases); hence the put call will block until consumer gets the task.

- can track progress of tasks in queue using .task_done() method
.task_done() acts as a blocking mechanism and doesn't return control back until all tasks are complete in queue.
'''