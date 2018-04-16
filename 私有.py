import sys
class Dog:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def test1(self):
        print("1111")

    def __test2(self):
        print("22222")

    def __del__(self):
        print("del")

dog=Dog("zhu",16)
dog.test1()
print(dog.age)
dog2=dog
print(sys.getrefcount(dog))
del dog
del dog2
# print(sys.getrefcount(dog))


# print(dog2.age)