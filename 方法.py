class Dog(object):

    #属性
    num=0
    #实例方法
    def __init__(self):
       Dog.num=Dog.num+1

    #类方法
    @classmethod
    def add_num(cls):
        cls.num=cls.num+1

    @staticmethod
    def print_menu():
        print("静态方法"+Dog.num)

dog=Dog()
Dog.add_num()
print(Dog.num)
Dog.print_menu()
