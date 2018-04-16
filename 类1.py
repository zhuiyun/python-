from 类 import MyClass


class Student(MyClass):
    def __init__(self, name1, score):
        self._name = name1
        self._score = score

    def info(self):
        print('姓名:%s,分数:%s' % (self._name, self._score))


student = Student('zhuiyun', '29')
student.f()
student.info()

