#获取键盘上输入的数据
name=input("请输入您的姓名:")
age=input("请输入您的年龄:")

print(f"您的姓名是：{name}\n年龄是：{age}")






#案例
#总金额
total=1000

#1.输入密码
password=input("请输入您的银行卡密码：")
print(f"密码正确，密码是{password}")

#2.输入取款金额，input输入的所有的数据都是字符串类型，在进行计算的时候要进行类型转换
num=input("请输入您的取款金额：")

#3.计算并输出余额
print(f"取款后您银行卡的余额是:{total-int(num)}")
