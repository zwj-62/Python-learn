# #字符串 基本操作-------->字符串不可变，也就是字符串无法进行修改
# s="Hello-Python"
# #获取字符串中的元素
# print(s[4])
# print(s[-8])
# #字符串的遍历
# for i in s:
#     print(i)
# #字符串的切片操作
# print(s[0:5:1])
# print(s[:5:])
#
# print(s[6:12:1])
#
# #步长为正数的情况：从前往后截取，负数：从后往前截取
# print(s[0:10:2])
# print(s[-1:-7:-1])




# #字符串的常用方法
# s="Hello-Python-Hello-World"
# #find（）查找指定字符串第一次出现的次数
# index=s.find("-")
# print(index)
# #count()统计子字符串在指定字符串中出现的次数
# c=s.count("o")
# print(c)
# #upper()转为大写
# s1=s.upper()
# print(s1)
# #lower()转小写
# s2=s.lower()
# print(s2)
# #split()将字符串按照指定字符串切割列表
# s4=s.split("-")
# print(s4)
# #strip()去除字符串两端的空格
# s5=s.strip()
# print(s5)
# #replace()将字符串中指定的字串替换为新内容
# s6=s.replace("-","*")
# print(s6)
# #startswith()/endswitch(),判断是否以此结尾
# print(s.startswith("Hello"))
# print(s.endswith("Python"))
# print(s)#字符串不变


#--------------------------字符串案例----------------
#接收一个邮箱，然后判断是否正确：至少包含一个. 和有且仅有一个@
# #方法一：
# #接收用户输入的邮箱
# mail=input("请输入邮箱:")
# #判断邮箱格式是否正确
# num1=mail.count("@")
# if num1==1:
#     num2=mail.count(".")
#     if num2>=1:
#         print("mail是合法邮箱")
# else:
#     print("mail不是一个合法邮箱")

# #方法二：
# #接收用户输入的邮箱
# mail=input("请输入邮箱:")
# #判断邮箱格式是否正确
# num1=mail.count("@")
# if mail.count("@")==1 and "." in mail:#在字符串中也可以使用in
#     print("mail是合法邮箱")
# else:
#     print("mail不是一个合法邮箱")

# #作业一：输入一个字符串，判断该字符串是否是回文（两边对称）
# str=input("请输入需要判断的字符：")
# lens=len(str)
# mid=int(lens/2)
# i=0
# while(mid>0):
#     if(str[i]!=str[len(str)-i-1]):
#         print("输入的字符串不是回文")
#         break
#     i=i+1
#     mid=mid-1
# if(mid==0):
#     print("输入的字符串是回文")


#作业二：用户输入10个字符串，反转后全部转为大写，然后还记录到列表中，最后将列表内容遍历输出
list=[]
for i in range(10):
    str=input("请输入一个字符串：")
    s=str.upper()
    list.append(s)
for j in range(10):
    print(list[j])
print(list)