import sys
print(sys.executable)
print(sys.version)

class Employment

	"""A sample Employee class"""

	def __inint__(self, first, last):
		self.first = first
		self.last = last

	@property
	def emial(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Herbiee', 'Hancock')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)