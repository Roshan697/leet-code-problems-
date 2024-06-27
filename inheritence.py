class Mammal:
    def walk(self):
        print("walk")



class Dog(Mammal):
    def bark(self):
        print("woof")
   
    

class Cat(Mammal):
    def mew(self):
        print("meow")
    

dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.mew()
            