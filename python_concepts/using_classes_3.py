
class OldResistor(object):

	def __init__(self, ohms):
		self._ohms = ohms

	def get_ohms(self):
		return self._ohms

	def set_ohms(self, ohms):
		self._ohms = ohms

class Resistor(object):

	def __init__(self, ohms):
		self.ohms = ohms
		self.voltage = 0
		self.current = 0

class VoltageResistance(Resistor):

	def __init__(self, ohms):
		super().__init__(ohms)
		self._voltage = 0

	@property
	def voltage(self):
		return self._voltage

	@voltage.setter
	def voltage(self, voltage):
		self._voltage = voltage
		self.current = self._voltage / self.ohms

class BoundedResistance(Resistor):

	def __init__(self, ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if ohms <= 0:
			raise ValueError("ohms must be > 0")
		self._ohms = ohms

class FixedResistance(Resistor):
	'''
	make ohms property immutable
	'''

	def __init__(self, ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if hasattr(self, '_ohms'):
			raise AttributeError("Can't set attribute")
		self._ohms = ohms

class MysteriousResistor(Resistor):

	def __init__(self, ohms):
		super().__init__(ohms)


	# only modify an object state in setter methods
	# also reading attributes should be very fast (accessing)
	@property
	def ohms(self):
		self.voltage = self._ohms * self.current

	@ohms.setter
	def ohms(self, ohms):
		self._ohms = ohms


if __name__ == "__main__":

	r0 = OldResistor(50e3)
	print(r0.get_ohms())

	r1 = Resistor(50e3)
	r1.ohms = 10e3
	print(f"Resistance is {r1.ohms}")
	r1.ohms += 5e3
	print(f"Resistance is {r1.ohms}")
	print("")

	r2 = VoltageResistance(1e3)
	print(r2.current)
	r2.voltage = 10
	print(r2.current)
	print(r2.voltage)
	print("")

	r3 = BoundedResistance(1e3)
	print(r3.ohms)
	r3.ohms = 2e3
	print(r3.ohms)
	print("")

	r4 = FixedResistance(1e3)
	print(r4.ohms)
	print("")

	r5 = MysteriousResistor(10e3)
	r5.current = 0.01
	print(r5.voltage)
	r5.ohms
	print(r5.voltage)
