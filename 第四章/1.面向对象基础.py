# #定义类
# class Car:
#     pass
# #创建对象
# c1=Car()
# #动态的为对象添加属性
# c1.color = "red"
# c1.brand="BNM"
# c1.name="X5"
# c1.price=5000
# print(c1)#直接输出是c1的内存地址
# print(c1.__dict__)#将对象中的所有属性以字典的形式输出出来
# print(c1.color)#如果只是想查看其中一个属性，则直接这样就可以输出
# print(c1.brand)
# print(c1.name)
# print(c1.price)

# #def定义在类的外面叫函数，定义在def里面叫做方法
# #定义类
# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中设置对应的属性
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         #self是类中定义的方法的第一个参数，表示当前创建的实例对象
#         self.color=c_color
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕")
#     #创建对象
# c1=Car("red","BNM","X5",5000)
# print(c1.__dict__)
# c2=Car("blue","奔驰","E300",6000)
# print(c2.__dict__)

# #--------------定义类 实例方法------------------------
# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中设置对应的属性
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         #self是类中定义的方法的第一个参数，表示当前创建的实例对象
#         self.color=c_color
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕")
#     #定义实例方法
#     def running(self):
#         print(f"{self.brand}{self.name}正在高速行驶")
#     def total_cost(self,discount,rate=0.1):
#         """
#         计算提车的总费用，车的价格税费
#         :param discount: 折扣
#         :param rate: 车税
#         :return: 提车的费用
#         """
#         total_cost=self.price*discount+rate*self.price
#         return total_cost
# #测试
# c1=Car("red","BNM","X5",80000)
#
# c1.running()
# count=c1.total_cost(discount=0.9,rate=0.1)
# print(count)
#
# c1=Car("blue","BNM","X5",80000)
# c1.running()
# total_cost=c1.total_cost(discount=0.8,rate=0.1)
# print(total_cost)

# #--------------定义类 实例方法------------------------
# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中设置对应的属性
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         #self是类中定义的方法的第一个参数，表示当前创建的实例对象
#         self.color=c_color
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕")
#     #定义实例方法
#     def running(self):
#         print(f"{self.brand}{self.name}正在高速行驶")
#     def total_cost(self,discount,rate=0.1):
#         """
#         计算提车的总费用，车的价格税费
#         :param discount: 折扣
#         :param rate: 车税
#         :return: 提车的费用
#         """
#         total_cost=self.price*discount+rate*self.price
#         return total_cost
#     #魔法方法
#     def __str__(self):
#         return (f"{self.color},{self.brand},{self.name},{self.price}")
#     def __eq__(self,other):#返回布尔类型的结果
#         return self.color==other.color and self.brand==other.brand and self.name==other.name and self.price==other.price
#     def __lt__(self,other):
#         return self.price<other.price
# #测试
# c1=Car("red","BNM","X5",80000)
# print(c1)
#
# c2=Car("blue","BNM","X5",90000)
# print(c2)
#
# print(c1==c2)
# print(c1<c2)#自动的返回俩价格对比的结果

#--------------定义类 实例方法------------------------
class Car:
    #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中设置对应的属性
    #类属性（所有实例对象共享）
    wheel=4
    tax_rate=0.1
    def __init__(self,c_color,c_brand,c_name,c_price):
        #self是类中定义的方法的第一个参数，表示当前创建的实例对象
        #实例属性
        self.color=c_color
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
        self.wheel=5
        print("Car类型的对象初始化完毕，对象属性已经添加完毕")
    #定义实例方法
    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶")
    def total_cost(self,discount,rate=0.1):
        """
        计算提车的总费用，车的价格税费
        :param discount: 折扣
        :param rate: 车税
        :return: 提车的费用
        """
        total_cost=self.price*discount+rate*self.price
        return total_cost
#测试
c1=Car("red","BNM","X5",80000)
print(c1.wheel)#实例对象在查找属性时，先查找实例属性，没有查找到才会查找类属性
print(c1.tax_rate)
c1.running()
count=c1.total_cost(discount=0.9,rate=0.1)
print(count)

c1=Car("blue","BNM","X5",80000)
c1.running()
total_cost=c1.total_cost(discount=0.8,rate=0.1)
print(total_cost)