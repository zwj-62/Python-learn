# #-------------------------函数---变量的作用域---------------------
# #全局变量
# num=100
# #定义函数
# def circle_area(r):
#     pi=3.14
#     area=pi*r**2
#     global num
#     num=10000
#     print("num1=",num)
#     return area
# #调用函数
# print(circle_area(10))
# print("num2=",num)


# #--------------------------------函数-传参方式-------------------------------
# #定义函数
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名：{name}，年龄{age},性别{gender}，城市{city}")
#     return{"name":name,"age":age,"gender":gender,"city":city}
#
# #传参一：位置参数
# stu1=reg_stu("zwj",15,"女","嘉兴")#把返回值放在stu中，然后用stu输出
# print(stu1)
#
# #传参二：关键字参数
# stu2=reg_stu(age=16,name="wed",gender="男",city="金华")
# print(stu2)
#
# #传参三：位置＋关键字
# stu3=reg_stu("zse",23,city="北京",gender="女")
# print(stu3)

#---------------------函数默认值-----------------------
#定义函数 默认参数要放在非默认参数之后
def reg_stu(name,age,gender,city="北京"):
    print(f"注册成功，姓名：{name}，年龄{age},性别{gender}，城市{city}")
    return{"name":name,"age":age,"gender":gender,"city":city}
stu1=reg_stu("zwj",18,"女")
print(stu1)
stu2=reg_stu("wdc",34,"男","嘉兴")
print(stu2)