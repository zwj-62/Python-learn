"""
封装：将数据（属性）和操作数据的方法绑定在一起，形成一个不可分割的整体，保护数据不被外部访问，通过访问器（getter）和修改器（setter）来访问和修改数据
1：私有属性：在属性名前加__，使其成为私有属性，不能在类的外部访问，只能在类的内部访问
2：公有属性：在属性名前不加__，使其成为共有属性，可以在类的外部访问，也可以在类的内部访问
"""

"""
继承：子类继承父类的属性和方法，子类可以拥有父类的属性和方法，也可以拥有自己的属性和方法
"""

"""
重写：子类重写父类的方法，实现子类自己的功能，可以调用父类的方法，也可以不调用父类的方法，通过super()方法调用父类的方法，实现子类自己的功能，也可以调用父类的方法，实现子类自己的功能
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
        #方法一：super（）方法名（）
        super().charge()
        #方法二：类名.方法名（self）
        Car.charge(self)
        print(f'{self.brand}{self.modle}正在加油')
#电车 #继承 只继承公有的属性和方法
class ElectricCar(Car):
    def charge(self):
        super().charge()
        Car.charge(self)
        print(f'{self.brand}{self.modle}正在充电')

if __name__ == '__main__':

    car=Car('Audi','A6','black','李昊')
    # print(car.brand)
    # print(car.modle)
    # print(car.color)
    # car.start()
    # car.run()

    car1=FuelCar('BWW','A4','red','张三')
    print(car1.brand)
    print(car1.modle)
    print(car1.color)
    car1.start()
    car1.run()
    car1.charge()

    car2=ElectricCar('Tesla','Model S','white','王五')
    print(car2.brand)
    print(car2.modle)
    print(car2.color)
    car2.start()
    car2.run()
    car2.charge()
