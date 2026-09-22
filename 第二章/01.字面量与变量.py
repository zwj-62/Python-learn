# # 字面量的写法
# print(100)#整数
# print(3.14)#小数
# print(True)#bool类型
# print(False)#布尔类型
# print("Hello World")#字符串类型
# print("-----------")#字符串类型
# print(None)#空值
# #布尔类型本质也是整形
# print(True +1)#2
# print(False - 1)#-1
#
#
#
# #案例
# base=20.7#基础播放量
# incr=50#每个月的播放量  也可以base,incr=20.7,50
# print("未来第一个月的播放总量",base+incr)
# print("未来第二个月的播放总量",base+incr+incr)
# print("未来第三个月的播放总量",base+incr+incr+incr)
#
# #标识符
# true=1
# print(true)
#
# name6="python"
# print(name6)
#


# #案例
# a=10
# b=20
# c=a
# a=b
# b=c
# print(a)
# print(b)


#练习
a=100
b=200
c=300
d=c
c=a
a=b
b=d
print(a,b,c)