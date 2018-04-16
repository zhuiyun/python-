class Dog(object):
    __instance = None
    def __new__(cls,name):
        if(cls.__instance==None):
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self,name):
        self.name=name



dog=Dog("dog")
print(dog.name)
dos2=Dog("dog2")
print(dos2.name)
print(id(dog))
print(id(dos2))