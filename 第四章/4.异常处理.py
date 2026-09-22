#异常处理
try:
    print("###########################################")
    print(my_name)
    print("###########################################")
except NameError as e:#要捕获的是NameEroorde cuowu
    print("程序运行出错，请联系管理员,异常信息为：",e)
print()
try:
    print("###########################################")
    print(1/0)
    print("###########################################")
except ZeroDivisionError as e:#要捕获的是NameEroorde cuowu
    print("程序运行出错，请联系管理员,异常信息为：",e)
print()

try:
    print("###########################################")
    print("ABC"[10])
    print("###########################################")
except IndexError as e:#要捕获的是NameEroorde cuowu
    print("程序运行出错，请联系管理员,异常信息为：",e)
print()
#可以使用Exception捕获所有的异常
try:
    print("##########################################")
    print("ABC",hello)
    print("##########################################")
except  Exception as e:
    print("运行出错，出现的异常为：",e)
finally:#无论程序运行是否出错，finally中的代码都会执行
    print("资源释放")
