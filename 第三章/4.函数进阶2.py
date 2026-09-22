#函数的参数类型
#加
def add(x,y):
    return x+y
#减
def sub(x,y):
    return x-y
#乘
def mul(x,y):
    return x*y
#除
def div(x,y):
    return x/y
#计算
def operation(x,y,oper):
    return oper(x,y)
#调用函数
print(operation(2,3,add))
print(operation(2,3,sub))
print(operation(2,3,mul))
print(operation(2,3,div))