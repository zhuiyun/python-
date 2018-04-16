class Dog(object):
    def run(self):
        print("run1")

class TT(object):
    def run(self):
        print("run2")

def instroduce(dog):
    dog.run()

instroduce(TT())
instroduce(Dog())