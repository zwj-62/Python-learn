# i=0
# while i<10:
#     print("人生苦短，我用python")
#     i=i+1
# else:
#     print("输入结束")





#while 案例：计算1-100之间所有偶数之和
total =0
i=1
while i<=100:
    if(i%2==0):
        total+=i
    i+=1
print("1-100偶数之和为：",total)