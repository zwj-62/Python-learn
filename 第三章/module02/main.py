# #导入模块
# import my_fun
# #使用模块中的功能
# #首先会对模块中的代码进行运行输出，再运行以下代码
# print(my_fun.PI)
# print(my_fun.NAME)
# my_fun.log_separator2()
# my_fun.log_separator3()


# #导入自定义模块中的功能
# from my_fun import log_separator1,log_separator2,PI
# log_separator1()
# log_separator2()
# print(PI)
#
from my_fun import *
#print(PI) #这里就会报错
log_separator1()
log_separator2()