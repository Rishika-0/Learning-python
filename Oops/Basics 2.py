class employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)    
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = employee('Rishika','Agarwal',50000)
emp_2 = employee('Test','User', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(employee.fullname(emp_1))

print(emp_1.__dict__)
print(emp_1.raise_amount)

emp_1.raise_amount = 1.05
print(emp_1.__dict__)

print(emp_1.raise_amount)
print(employee.raise_amount)
print(emp_2.raise_amount)

print(employee.__dict__)

print(employee.num_of_emps)
