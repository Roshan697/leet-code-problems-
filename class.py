class Person:
    name = "Roshan"
    occupation = "software dev"
    networth = 100000000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()
a.name = "Shubham"
a.occupation = "Accountant"

b = Person()
b.name = "Nitika"
b.occupation  = "HR"
a.info()
b.info()
    