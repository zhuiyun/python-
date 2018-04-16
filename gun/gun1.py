class Person(object):
    def __init__(self,name):
        super(Person,self).__init__()
        self.name=name
        self.gun=None
    def anZhuangZiDan(self,danjia,zidan):
        danjia.add_Zidan(zidan)

    def add_DanJia(self,gun,danjia):
        gun.addDanJia(danjia)

    def na_qiang(self,gun):
        self.gun=gun

    def __str__(self):
        if self.gun:
            return "姓名:%s,信息%s"%(self.name,self.gun)
        else:
            return "姓名:%,没有枪"


class Gun(object):
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name=name
        self.danjia_temp=None

    def addDanJia(self,danjia):
        self.danjia_temp=danjia

    def __str__(self):
        if self.danjia_temp:
            return "枪的信息%s,有弹夹,%s" % (self.name,self.danjia_temp)
        else:
            return "枪的信息%s,没有弹夹"%(self.name)

class DanJia(object):
    def __init__(self,num):
        super(DanJia,self).__init__()
        self.num=num
        self.zidan_list=[]

    def add_Zidan(self,zidan):
        self.zidan_list.append(zidan)

    def __str__(self):
        return "数量%s"%(len(self.zidan_list))

class ZiDan(object):
    def __init__(self,shashangli):
        super(ZiDan,self).__init__()
        self.shashangli=shashangli

def main():
    laowang=Person('老王')
    ak47=Gun("Ak47")
    danjia=DanJia(20)
    for i in range(19):
        zidan=ZiDan(10)
        laowang.anZhuangZiDan(danjia,zidan)
    laowang.add_DanJia(ak47,danjia)
    laowang.na_qiang(ak47)
    # print(danjia)
    print(laowang)

if __name__ == '__main__':
    main()
