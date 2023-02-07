'''
Subprocesses run independently from parent process (the python interpreter)
'''

import subprocess
import time
import os

process = subprocess.Popen(
	["echo", "Hello from the child!"], # cmds
	stdout=subprocess.PIPE # pipe process back to parent
)

process2 = subprocess.Popen(["sleep", "0.8"])

out, err = process.communicate() # returns output of prior subprocess

print(out.decode("utf-8"))

# can poll processes while they're running
while process2.poll() is None:
	print("Working...")

	#can do some other stuff
	time.sleep(0.2)

print("Exit status of process2: ", process2.poll())
print("")

def run_sleep(period):
	proc = subprocess.Popen(["sleep", str(period)])
	return proc

start = time.time()
procs = []
for _ in range(10):
	proc = run_sleep(0.5)
	procs.append(proc)

for proc in procs:
	proc.communicate() # waits for the output of process

print("Done!")

total_time = time.time() - start
print(f"Total time was {total_time} seconds")
print("")

def run_openssl(data):
	''' Purpose is to simulate a CPU intensive process '''
	env = os.environ.copy()
	env["password"] = b"secret"
	proc = subprocess.Popen(
		["openssl", "enc", "-des3", "-pass", "env:password"],
		env=env,
		stdin=subprocess.PIPE, # socket conn between this child and parent (can read input from parent)
		stdout=subprocess.PIPE # can collect child output
	)
	proc.stdin.write(data)
	proc.stdin.flush()
	return proc

def run_md5(input_stdin):
	proc = subprocess.Popen(
		["md5"],
		stdin=input_stdin,
		stdout=subprocess.PIPE
	)

	return proc

def chaining_processes():
	pass

if __name__ == "__main__":

	input_procs = []
	for _ in range(5):
		data = os.urandom(100) # 100 bytes random data
		proc = run_openssl(data)
		input_procs.append(proc)

	# pipe input_procs ssl outputs into hash_procs
	hash_procs = []
	for proc in procs:
		hash_proc = run_md5(proc.stdout)
		hash_procs.append(hash_proc)

	# wait for ssl input procs to complete
	for proc in input_procs:
		proc.communicate()

	# get final hash processes output
	for proc in hash_procs:
		try:
			out, _ = proc.communicate(timeout=1)
			print(out)
		except subprocess.TimeoutExpired:
			proc.terminate()
			proc.wait()
		print("Exit status", proc.poll())
