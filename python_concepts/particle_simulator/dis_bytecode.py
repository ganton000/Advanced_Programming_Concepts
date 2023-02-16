import dis

from particle import ParticleSimulator

dis.dis(ParticleSimulator.evolve)


'''
This outputs a list of bytecode instructions for each line in the function
'''