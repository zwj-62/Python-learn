# #打印出一个长度为10，宽度为5的长方形，用*表示1
# m=int(input("请输入长方形的长："))
# n=int(input("请输入长方形的宽："))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")#print是自动换行的，如果不想换行，则加入end=" ",意思是每次输出以什么结束，默认是\n,所以我们想要修改则要自己修改
#     print()

#案例：打印九九乘法表
for i in range(1,10):#外层循环，控制的是行数 范围是1 2 3 4 5 6 7 8 9
    for j in range(1,i+1):#内层循环，控制的是每行的内容 从1 到i
        print(f'{j}*{i}={i*j}',end=' ')
    print()