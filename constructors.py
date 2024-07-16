class Person:
    name = "name of the employee"
    occupation = "designation"
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = Person()
a.name = "Div"
a.occ = "HR"
a.info()        