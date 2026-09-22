#案例一：计算n的阶乘
#递归调用 ，指的是在函数中自己调用自己的情况
def jc (n):
    if n==1:
        return 1
    return n*jc(n-1)
result=jc(10)
print(result)