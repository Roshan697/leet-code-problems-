class Person:
    def __init__(self,name) -> None:
        self.name = name
    def talk(self):
        print(f"hi i am {self.name}")


john = Person("john smith")
print(john.name)
john.talk() 

ted = Person("Ted Bundy")
ted.talk()
