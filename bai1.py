class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
person=Person('Lan',16)
print(person.get_age())
print(person.get_name())
    