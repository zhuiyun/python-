class CarStore(object):
    def order(self,name,money):
        if(money>500000):
            print("预定一辆%s,定金%s"%(name,money))
            return Car()
        else:
            return Car()

    # def __new__(cls):
    #     print("new")

class Car(object):
    def move(self):
        print("移动")

    def stop(self):
        print("停下")

carStore=CarStore()
car=carStore.order("本田",1000000)
car.move()
car.stop()