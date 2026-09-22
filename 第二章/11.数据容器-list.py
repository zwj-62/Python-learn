# #列表操作
# #定义列表
# s=[45,43,67,49,"hello",True,"A"]
# print(type(s))
# #获取列表的元素
# print(s[0])#正向索引是从0开始
# print(s[-7])#反向索引是从-1开始
# print(s[1])
# print(s[-6])
# print(s[4])
# print(s[-3])
# #修改列表元素
# s[5]="ABC"
# print(s)
# #删除一个元素
# del s[6]
# print(s)
# #遍历列表
# for i in s:
#     print(i)
# #--------------列表-切片---------------------
# s=["A","B","C","D","E","F","G","H","I","J"]
# print(s[0:5:1])#包含s[0]不包含s[5],跳数为1
# print(s[:5:])
# print(type(s[0:5:1]))
# print(s[0:6:2])#跳数为2
# print(s[0:10:3])
# print(s[0:-2:1])#不包括s[-2]

# #------------------列表list常用的方法--------------
# #定义一个list列表
# s=[10,4,20,30,23,40,60,70,80,90,100]
# #在list尾部添加一个元素‘
# s.append(110)
# print(s)
# #insert(),在指定索引之前，添加一个元素
# s.insert(2,24)
# print(s)
# #removez(),删除第一个匹配的元素
# s.remove(40)
# print(s)
# #pop()删除列表中指定位置的元素，并返回（如果未指定，则默认删除最后一个）
# e=s.pop(5)
# print(e)
# print(s)
# e=s.pop()
# print(e)#默认删除最后一个
# print(s)
# #sort()该方法是将list列表中的元素进行排序
# s.sort()
# print(s)
# #reverse()：反转列表元素
# s.reverse()
# print(s)
#
#
# #列表的案例一：用户输入10个数字，然后存储到一个列表中，将其排序，输出最大值最小值
# #定义一个列表
# num_list=[]
# #将用户输入的10个数字存入列表
# for i in range(10):
#     num=int(input("请输入一个数字："))
#     num_list.append(num)
# #排序
# num_list.sort()
# print(num_list)
# #输出最大值，最小值和平均值
# print("最小值：",num_list[0])
# print("最大值：",num_list[-1])
# total=0
# for i in range(10):
#     total+=num_list[i]
# total=total/10
# print(total)
# #也可以用sum（） 来求列表的总和，len（）是获取列表的长度
# ave=sum(num_list)/len(num_list)
# print("平均值：",ave)
#
# #案例二：h合并两个列表，并去除重复数据
# num_list1=[12,32,45,65,745,324,65,76,90]
# num_list2=[3,5,63,64,76,91]
# #先合并两个列表
# #解包操作：将列表这一类的容器解开成一个独立的元素
# #组包：将多个值并列到一个容器
# num_list=[*num_list1,*num_list2]
# print("解包合并后的数据",num_list)
# #直接使用+来合并两个元素
# num_list3=num_list1+num_list2
# print("使用+合并列表：",num_list3)
# #使用for循环合并
# for num in num_list2:
#     num_list1.append(num)
# print("for合并后的列表",num_list1)
# #去除重复数据
# new_list=[]
# for num in num_list1:
#     # 判断一个元素是否在列表中
#     if num not in new_list:
#         new_list.append(num)
# print("去除重复数据后的列表：",new_list)
# new_list.sort()
# print("对最后的列表进行排序：",new_list)
#
# #案例三：生成1-20的平方列表
# num_list=[]
# for i in range(1,21):
#     i*=i
#     num_list.append(i)
# print(num_list)
# #方式二：列表推导式------>就是按照一定的规则快速生成一个列表的方法：
# 语法格式一：[要插入的值 for i in 序列/列表]
#语法格式二：[要插入的值 for i in 序列/列表 if 条件]
# num_list2=[i*i for i in range(1,21)]
# print(num_list2)
#案例四：从列表中提取出所有的偶数，并计算平方，然后放入到一个新的列表中
num_list=[12,32,45,77,80,92,33,57,97,110,111,122]
#语法格式二：[要插入的值 for i in 序列/列表 if 条件]
new_list=[i*i for i in num_list if i%2==0]
print(new_list)