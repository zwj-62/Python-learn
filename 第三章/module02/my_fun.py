__all__ = ["log_separator1","log_separator2"]#意思是使用import my_fun *的时候只会导入中括号中的这些函数
#常量，不会发生变化的数据。常量的名称为全大写
PI=3.1415926
NAME="黑马*涛哥"

#函数
def log_separator1():
    print("-"*30)#-重复输出30次
def log_separator2():
    print("+"*30)
def log_separator3():
    print("*"*30)
#测试函数
#__name__:python中的内置变量，表示当前模块的名字（直接运行该模块，__name__的值就是该模块：当该模块被导入的时候，__name__就是模块名称
print(__name__)
log_separator1()
#执行 当前文件则会直接执行以下代码，但是作为模块导入，则以下的代码则不执行
if __name__=="__main__":
    log_separator2()
    log_separator3()