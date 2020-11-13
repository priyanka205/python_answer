# I am creating class for office

class Headoffice:
    def __init__(self, role, name, salary):
        self.role = role
        self.name = name 
        self.salary = salary

    def get_role(self):
        return self.role

    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary

class Branchoffice:
    def __init__(self, role, name, age):
        self.role = role
        self.name = name 
        self.age = age

    def retirement(self):
        # return 50-self.age
        return (f"{self.name} is retiring in {50-self.age} years.")
  





o = Headoffice("Manager","James", 5000)

print(o.get_role())
print(o.get_name())
print(o.get_salary())

b = Branchoffice("Accountant","Tisa",20)
print(b.age)
r = b.retirement()
print(r)
