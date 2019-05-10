# Python Object-Oriented Programming


# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('Matthew', 'Berning', 80000)
# emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Matthew', 'Berning', 80000)
emp_2 = Employee('Test', 'User', 60000)

# print(Employee.__dict__)
print(Employee.num_of_emps)
