class Cat:
    def __init__(self,newName,newAge):
        self.name=newName
        self.age=newAge
        print("初始化")
    def __str__(self):
        return "hhhhh"
    def eat(self):
        print("eat方法")
    def run(self):
        print("run方法")
    def instro(self):
        print("%s岁的%s猫喜欢吃鱼"%(self.age,self.name))

cat=Cat("tom",15)
# cat.eat()
# cat.run()
# cat.name="tom"
# cat.age=18.2
# cat.instro()
# cat.__str__()
print(cat)

h=Cat("catty",16)
# h.name="hhh"
# h.age=10
# h.instro()