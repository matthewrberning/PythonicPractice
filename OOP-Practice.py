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


# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_string):
#         first, last, pay = emp_string.split('-')
#         return cls(first, last, pay)


# emp_1 = Employee('Matthew', 'Berning', 80000)
# emp_2 = Employee('Test', 'User', 60000)

# Employee.set_raise_amount(1.05)

# # print(Employee.__dict__)
# # print(Employee.num_of_emps)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# # first, last, pay = emp_str_1.split('-')

# # new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Matthew', 'Berning', 80000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2019, 5, 9)

print(Employee.is_workday(my_date))
