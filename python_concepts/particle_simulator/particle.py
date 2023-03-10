from typing import List
from random import uniform

from matplotlib import pyplot as plt
from matplotlib import animation
from memory_profiler import profile

class Particle:

	def __init__(self, x: str, y: str, ang_vel: int) -> None:
		self.x = x
		self.y = y
		self.ang_vel = ang_vel

class ParticleSimulator:

	def __init__(self, particles: List[Particle]) -> None:
		self.particles = particles

	@profile
	def evolve(self, dt: int) -> None:
		timestep = 0.0001
		nsteps = int(dt/timestep)

		for i in range(nsteps):
			for p in self.particles:
				norm = (p.x**2 + p.y**2)**0.5
				v_x = -p.y/norm # opp/hyp
				v_y = p.x/norm

				# displacement
				d_x = timestep * p.ang_vel * v_x
				d_y = timestep * p.ang_vel * v_y

				p.x += d_x
				p.y += d_y

def visualize(simulator: ParticleSimulator) -> None:
	X = [p.x for p in simulator.particles]
	Y = [p.y for p in simulator.particles]

	fig = plt.figure()
	ax = plt.subplot(111, aspect="equal")
	line, = ax.plot(X,Y, "ro")

	#Axis lims
	plt.xlim(-1, 1)
	plt.ylim(-1, 1)

	def init():
		line.set_data([], [])
		return line,

	def animate(i):
		simulator.evolve(0.01)
		X = [p.x for p in simulator.particles]
		Y = [p.y for p in simulator.particles]
		line.set_data(X,Y)
		return line,

	# call animate every 10 ms
	anim = animation.FuncAnimation(
		fig,
		animate,
		init_func=init,
		blit=True,
		interval=1000
	)
	plt.show()

def test_visualize():

	particles = [
		Particle(0.3, 0.5, 1),
		Particle(0.0, -0.5, -1),
		Particle(-0.1, -0.4, 3)
	]

	simulator = ParticleSimulator(particles)
	visualize(simulator)

def benchmark():
    particles = [
        Particle(
			uniform(-1.0, 1.0),
			uniform(-1.0, 1.0),
			uniform(-1.0, 1.0)
		)
		for i in range(10000)
	]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

if __name__ == "__main__":

	#test_visualize()
	#test_evolve()
	benchmark()

'''

BENCHMARK:::
cmd:
time python particle.py ## time is built-in Unix library

outputs:
real - actual time of process from start to finish (as it timed with stopwatch)
## good for I/O time spent

user - cumulative time spent by all CPUs during computation
## good for CPU performance


sys - cumulative time spent by all CPUs with sys-related tasks (such as memory allocation)


PYTEST:::
pytest ./tests/test_particle.py::test_evolve


cProfile:::
written in C, small overhead, suitable as general-purpose profiler

python3 -m cProfile particle.py

## sort by  and output to file prof.out
python3 -m cProfile -s tottime -o prof.out particle.py

ncalls: Number of times function was called within script
tottime: total time spent in function, without taking into acount calls to other functions. *** tottime most important metric for bottlenecks ***
cumtime: time spent in function, including other function calls.
percall: time spent for a single call of the function (cumtime/ncalls)
filename:lineno: obvious


Visualizing profilers:::
Using qcachegrind (brew install)
pip install pyprof2calltree to convert prof.out to qcachegrind readable input via

pyprof2calltree -i prof.out -o prof.calltree
qcachegrind prof.calltree

Can also use gprod2dot for call graph

Line-By-Line Profiling:::
pip install line_profiler ## https://github.com/rkern/line_profiler

use the @profile decorator to functions intended to be monitored
then run kernprof -l -v particle.py

-l: to use line_profiler function
-v: to print results to screen

line: line number run
hits: number of times that line was run
time: execution time of line in microseconds
per hit: time/hits
% time: fraction of total time spent executing that line *** most important ***
line contents: content of the line


Memory Optimization:::

pip install memory_profiler psutil

add @profile to function intended to be monitored

mprof run particle.py


Note: mprof run --multiprocess particle.py enables profiling against multiple processes.


__slots__ helps reduce memory footprint, by avoiding storing the variables of the instance in an internal dictionary. Drawbacks: prevents addition of attributes outside of the ones defined in __slots__
'''