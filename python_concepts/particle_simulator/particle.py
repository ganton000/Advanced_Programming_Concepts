from typing import List

from matplotlib import pyplot as plt
from matplotlib import animation

class Particle:

	def __init__(self, x: str, y: str, ang_vel: int) -> None:
		self.x = x
		self.y = y
		self.ang_vel = ang_vel

class ParticleSimulator:

	def __init__(self, particles: List[Particle]) -> None:
		self.particles = particles

	def evolve(self, dt):
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