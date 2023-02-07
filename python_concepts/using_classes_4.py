
class MyObject(object):

	def __init__(self):
		self.public_field = 5
		self.__private_field = 10

	@classmethod
	def get_private_field_of_instance(cls, instance):
		return instance.__private_field

class MyChildObject(MyObject):

	def get_private_field(self):
		return self.__private_field

class MyBaseClass(object):

	def __init__(self, value):
		self.__value = value

	def get_value(self):
		return self.__value

class MyClass(MyBaseClass):

	def get_value(self):
		return str(self._MyBaseClass__value)

class MyIntegerSubclass(MyClass):

	def get_value(self):
		## Attribute is tied to the class name
		# return int(self._MyClass__value)
		## better to use protected variables for inherited values
		## that shouldn't be accessed directly (outside of children classes)
		return int(self._MyBaseClass__value)

class ApiClass(object):

	def __init__(self):
		self._value = 5
		self.__private = 5

	def get(self):
		return self._value

	def get_private(self):
		return self.__private

class Child(ApiClass):

	def __init__(self):
		super().__init__()
		self._value = "hello"
		self._private = "hello"

if __name__ == "__main__":
	foo = MyObject()
	print(MyObject.get_private_field_of_instance(foo))
	print(foo.public_field)
	#print(foo.__private_field_of_instance) ## AttributeError
	print("")

	child_foo = MyChildObject()
	#child_foo.get_private_field() ## AttributeError
	## Direct Access to parent's private attribute in child doesn't work.
	## Can be done using _ParentClassName
	print(child_foo._MyObject__private_field)

	# private inherited attribute can be shown here
	print(child_foo.__dict__)

	# can still be accessed/mutated

	del child_foo.__dict__["_MyObject__private_field"]

	print(child_foo.__dict__)
	print("")

	bar = MyClass(5)
	print(repr(bar.get_value()))

	child_bar = MyIntegerSubclass(5)
	print(repr(child_bar.get_value()))

	# overrides parent's protected attribute!
	a = Child()
	print("\nProtected attr in parent is mutated: ")
	print(a._value)
	print(a.get())

	print("\nPrivate attr in parent remains unchanged: ")
	print(a._private)
	print(a.get_private())





'''
Two underscores := "private" to the class
One underscore := "protected"; i.e. can be used by subclasses
No underscore prefix := public

Best to use private attributes when avoid naming conflicts within subclasses.
'''