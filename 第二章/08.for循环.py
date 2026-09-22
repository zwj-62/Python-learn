# msg=input("请输入需要遍历的字符串：")
# for i in msg:#i表示遍历出来的元素，msg 表示要遍历的而数据
#     print(i)
# else:
#     print("遍历结束")

# #案例一：计算1-100之间的奇数之和
# i=1
# total=0
# for i in range(1,101,2):#range是不包括101的，所以只到100.范围为1-100，每次是添加2，原本默认是添加1
#     total+=i
# print(total)
#
#
# #案例一：计算1-100之间的奇数之和
# i=1
# total=0
# for i in range(1,101):#range是不包括101的，所以只到100.范围为1-100，每次是添加2，原本默认是添加1
#     if (i%2==1):
#         total+=i
# print(total)

#案例二：输出100-500之间所有3的倍数
total=0
for i in range (100,501):
    if(i%3==0):
        print(i)
        total+=i
print(total)


