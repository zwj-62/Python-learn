#导入整个模块
print("导入整个模块案例：")
import random
for i in range(5):
    print(random.randint(1,100))#生成一个1-100之间的随机整数
print()

import random as rd
print(rd.randint(1,100))
#导入模块中的某个功能
print("导入某个模块其中一个功能的案例：")
from random  import randint
print(randint(1,100))

from random import randint as rint
print(randint(1,100))

print("导入模块的所有功能：")
from random import*
print(randint(1,100))#这里可以直接使用功能名调用函数
