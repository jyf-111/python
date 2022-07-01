class Animal:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

dog = Animal('jyf',20)
dog.sit()
dog.roll_over()


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def sit(self):
        print(f"dog sit")

Dog('hihi',22).sit()