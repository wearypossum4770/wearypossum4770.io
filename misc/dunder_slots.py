class MyClass(object):
	__slots__ = ['name', 'identifier']
	def __init__(self, name, identifier):
		self.name = name
		self.identifier = identifier
		self.set_up()
