#Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee('Matthew', 'Berning', 80000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)
print(emp_1.email)
print(emp_2.email)
