"""
多态：同一个方法，不同的实现方式，不同的对象，调用同一个方法，结果不同

"""
class Car:
    def __init__(self,brand,model,color,owner):
        self.brand=brand
        self.modle=model
        self.color=color
        self.__owner=owner#私有属性，只能在类的内部访问

    def start(self):
        print(f'{self.__owner}{self.brand} {self.modle}正在启动.....')#访问私有属性，需要通过类的内部方法
        self.__control_fule()#调用私有方法，需要通过类的内部方法
    def run(self):
        print(f'{self.__owner}{self.brand} {self.modle}正在行驶.....')#访问私有属性，需要通过类的内部方法
    def __control_fule(self):
        print(f'{self.__owner}正在控制油门')
    def charge(self):
        print(f'{self.__owner}正在补充燃油')


#燃油车 #继承 只继承公有的属性和方法
class FuelCar(Car):
    def charge(self):
        print(f'{self.brand}{self.modle}正在加油')
#电车 #继承 只继承公有的属性和方法
class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand}{self.modle}正在充电')


#补充燃料函数
def handle_charge(car: Car):
        car.charge()

if __name__ == '__main__':
    handle_charge(FuelCar('丰田','卡罗拉','红色','张三'))
    handle_charge(ElectricCar('特斯拉','Model 3','白色','李四'))
