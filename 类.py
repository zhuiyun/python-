class MyClass(object):
    i=123
    def __init__(self,name):
        self.name=name;

    def __say(self):
        self._eat()
        print('好像是私有方法')


    def _eat(self):

        print("不知道")

    def f(self):
        self.__say()
        return "hello world"
claz=MyClass("zhuiyun")

print(claz.f())
print(claz.i)