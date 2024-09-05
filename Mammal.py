class Mammal:
    __kingdom="animal"
    def __init__(self,name,type1,sound):
        self.name=name
        self.type=type1
        self.sound=sound
        #__kingdom="animal"
    def make_sound(self):
        return f"{self.name} make {self.sound}"
    def get_kingdom(self):
        return self.__kingdom
    def info(self):
        return f"{self.name} is of type {self.type}"

Thu=Mammal("Dog","Domestic","Bark")
print(Thu.make_sound())
print(Thu.get_kingdom())
print(Thu.info())

 
