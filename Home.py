class Home:
    def __init__(self,area,money):
        self.area=area
        self.money=money
        self.leftArea=area
        self.jiaju=[]

    def __str__(self):
        return "房子面积%s,价值%s,剩余面积%s,已有家具%s"%(self.area,self.money,self.leftArea,str(self.jiaju))

    def addJiaju(self,item):
        self.leftArea=self.leftArea-item.area
        self.jiaju.append(item.name)
        return self

class Jiaju:
    def __init__(self,name,area):
        self.name=name
        self.area=area



h=Home(206.6,1000000000)
print(h)
b=Jiaju("床",6)
c=Jiaju("桌子",4)
h.addJiaju(b).addJiaju(c)

print(h)