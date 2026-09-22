# #break 和 continue 只能出现在循环内部
# while (1):#或则使用while True:也可以
#     name = input("请输入您的用户名：")
#     password = input("请输入正确的密码：")
#     #如果输入为空
#     if name =="" or password == "":
#         print("输入为空，请重新输入用户名和密码")
#         continue#结束当前循环，继续进行下一次循环
#     if name == "admin" and password == "666888":
#         print("登录成功，欢迎进入B站！")
#         break#跳出循环，也就是结束while这部分代码的全部内容
#     elif name == "zhangsan" and password == "123456":
#         print("登录成功，欢迎进入B站！")
#         break
#     elif name == "taoge" and password == "456789":
#         print("登录成功，欢迎进入B站！")
#         break
#     else:
#         print("输入用户名和密码错误，重新输入")


# #综合案例二：猜数字的小游戏
# import random
# random_number=random.randint(1,100)#使用random随机输出一个1-100的数字
# while True:
#     number=int(input("请输入您猜的数字："))
#     if number==random_number:
#         print(f"您猜对啦！,数字就是{random_number}")
#         break
#     elif number>random_number:
#         print("大啦，请重新猜测吧~")
#     else:
#         print("小啦，请重新猜测吧~")


#作业一：1-1000之内的数字所有5 的倍数的数字都累加起来
total=0
for i in range(1,1001):
    if(i%5==0):
        total+=i
print(total)
#作业二：统计字符串“akiwksjakdiklowiqaanvbmvaxnsjsdjkaaxkkjd"字符串中有多少个a k
num1=0
num2=0
for i in "akkiwksjakdiklowiqaanvbmvaxnsjsdjkaaxkkjd":
    if i =="a":
        num1+=1
    elif i =="k":
        num2+=1
print(f"a的个数有{num1}个")
print(f"k的个数有{num2}个")
