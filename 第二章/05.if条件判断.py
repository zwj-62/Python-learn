# score=600
# if score>680:
#     print("欢迎你来清华读书")
#     print("也恭喜你即将踏入精彩的大学生活")
# print("--------------------")

# #案例一
# #完成B站登录功能的实现
# ok_acount="188888888"
# ok_password="666888"
# #1.接受用户输入账号和密码
# acount=input("请输入您的B站账号：")
# password=input("请输入您的B站密码：")
# #2.正确进入首页
# if acount==ok_acount and password==ok_password:
#     print("登录成功~")
#     print("进入B站首页~")
# #3.错误提示信息
# if acount!=ok_acount or password!=ok_password:
#     print("登陆失败！")
#     print("登录账号或则密码不正确！")

# #案例二，if else
# #完成B站登录功能的实现
# ok_acount="188888888"
# ok_password="666888"
# #1.接受用户输入账号和密码
# acount=input("请输入您的B站账号：")
# password=input("请输入您的B站密码：")
# #2.正确进入首页
# if acount==ok_acount and password==ok_password:
#     print("登录成功~")
#     print("进入B站首页~")
# else :
#     print("登陆失败！")
#     print("登录账号或则密码不正确！")

# #作业二，根据用户输入的年龄判断是否成年
# age=int(input("请输入您要判断的年龄："))
# if age>=18:
#     print("成年了")
# else:
#     print("未成年")

# #if elif else语句判断
# #判断输入的数字是0 还是正数 还是负数
# num=int(input("请输入你需要判断的数字："))
# if num==0:
#     print("您输入的数字是0")
# elif num>0:
#     print("您输入的数字是正数")
# else:
#     print("您输入的数字是负数")


#
# #复杂的登录判断
# acount=input("请输入您的登录用户名：")
# password=int(input("请输入您的密码："))
# if acount == "admin" and password==666888:
#     print("登录成功1")
# elif acount=="root" and password==547527:
#     print("登录成功2")
# elif acount == "zhangsan" and password==123456:
#     print("登录成功3")
# else:
#     print("登陆失败，用户名或则密码错误")


#复制案例：判断三条边是否可以构成三角形，如果构成三角形后，是什么三角形
#  构成三角形的条件：两边之和大于第三条边
# 三遍都相等：等边三角形
# 两边相等：等腰三角形
# 三边都不想等：普通三角形
# """
a=int(input("请输入第一条边的边长："))
b=int(input("请输入第二条边的边长："))
c=int(input("请输入第三条边的边长："))
#判断是否构成三角形
if (a+b)>c and (b+c)>a and (c+a)>b:
    print("三条边能够构成三角形")
    if a==b==c:
        print("该三角形是等边三角形")
    elif a==b or a==c or b==c:
        print("该三角形是等腰三角形")
    else:
        print("该三角形是普通三角形")
else:
    print("这三条边并不能构成三角形")