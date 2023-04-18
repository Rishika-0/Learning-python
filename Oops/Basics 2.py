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
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

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
emp_1.set_raise_amt(1.06)
print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'Aditi-Sharma-70000'
emp_str_2 = 'Vidush-Agarwal-30000'
emp_str_3 = 'Shivi-Rathod-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
