class Animal:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def spek(self):
        return self.__age
    

class Dog(Animal):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def spek(self):
        return self.__name
    

s = Dog('Dog','23')
print(s.__name)


