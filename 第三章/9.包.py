#1.导入模块
# import utils.my_fun
#
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()
#
#
# from utils import my_fun
# my_fun.log_separator3()
#如果使用这种方式导入包中的所有模块，需要加__all__=[],不然就不可以导入
from utils import*
my_fun.log_separator3()
my_fun.log_separator1()
print(my_var.PI)