"""
多继承：一个类可以继承多个父类的属性和方法
"""
from tarfile import version


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

    def stop (self):
        print(f'{self.__owner}{self.brand} {self.modle}正在停止.....')

    def __control_fule(self):
        print(f'{self.__owner}正在控制油门')

    def charge(self):
        print(f'{self.__owner}正在补充燃油')

class HuaWeiAirDriving:
    def __init__(self,version='1.0'):
        self.version=version
    def run(self):
        print(f'正在使用华为智能驾驶系统{self.version}正在驾驶....')

class WenJieCar(Car,HuaWeiAirDriving):
    def __init__(self,brand,model,color,owner,version='1.0'):
        Car.__init__(self,brand,model,color,owner)#直接从父类里继承就可以了
        HuaWeiAirDriving.__init__(self,version)
        def run(self):
            Car.run(self)
            HuaWeiAirDriving.run(self)


if __name__=='__main__':
    c=WenJieCar('BMW','X5','pink','zwj')#用Car中的init
    print(WenJieCar.__mro__)#查看类的继承关系
    print(c.__dict__)
    c.run()