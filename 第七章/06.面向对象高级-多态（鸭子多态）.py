'''
多态：同一个方法，不同的实现方式，不同的对象，调用同一个方法，结果不同
鸭子多态：如果它走起路来像鸭子，叫起来像鸭子，那么它就是一只鸭子，也就是无论是什么对象，如果它有鸭子的特征，那么它就可以被看作是鸭子

'''
class Duck:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')

class Pig:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')


def go_swimming(duck:Duck):
    duck.swimming()

if __name__ == '__main__':
    go_swimming(Duck('小鸭',4))
    go_swimming(Dog('旺财',5))
    go_swimming(Pig('佩奇',2))