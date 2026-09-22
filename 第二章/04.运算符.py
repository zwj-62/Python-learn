#算术运算符：+ - * / // %  **
print("10+4=",10+4)
print("10-4=",10-4)
print("10*4=",10*4)
print("10/4=",10/4)
print("10//4=",10//4)
print("10%4=",10%4)
print("10**4=",10**4)

#算术运算符优先级---->** --->* / //%---->+ -
print("0.1+10/4**2=",0.1+10/4**2)


#案例 在进行浮点数运算的时候可能出现不精准的情况，这是因为计算机使用的是二进制加减法，没办法把所有的小数都表示出来，这是正常的
x=int(input("请输入第一个数："))
y=int(input("请输入第二个数："))
print("x+y=",x+y)
print("x-y=",x-y)


#练习一，计算三个输入数的平均数
num1=float(input("请输入第一个数："))
num2=float(input("请输入第二个数："))
num3=float(input("请输入第三个数："))
num4=num1+num2+num3
ave=num4/3
print(f"三个数的平均数是：{ave}")

#练习二，要求输入梯形的上底下底高然后计算梯形面积
a=float(input("请输入梯形上底的长度："))
b=float(input("请输入梯形下底的长度："))
h=float(input("请输入梯形的高："))
S=(a+b)*h/2
print(f"梯形的面积是{S}")

#练习三、要求输入圆的半径，然后计算圆的周长和面积
r=float(input("请输入圆的半径："))
C=2*3.14*r
S=3.14*r*r
print(f"圆的周长是{C}，圆的面积是{S}")

#练习四、身体质量指标BMI的计算
kg=float(input("请输入您的体重kg："))
h=float(input("请输入您的身高m："))
BMI=kg/(h*h)
print(f"您的BMI是：{BMI}")

num=85
num+=10
print("num+=10后，num=",num)#95

num-=10
print("num-=num后，num=",num)#85

num*=10
print("num*=10后，num=",num)#850

num/=10
print("num/10=后，num=",num)#85.0

num//=10
print("num//=10后，num=",num)#8

num%=3
print("num%=3后，num=",num)#2

num**=3
print("num**=3后，num=",num)#8

print("100=100嘛：",100==100)
print("100!=100嘛：",100!=100)
print("100>100嘛：",100>100)
print("100<100嘛:",100<100)
print("100>=100嘛：",100>=100)

#案例一，键盘输入一个整数，判断是否在10-20之内
num=int(input("请输入一个整数："))
print(f"{num}在10-20之间：",num>=10 and num<=20 )

#案例二，输入一个整数，判断这个数字是否不在10-20之间
num=int(input("请输入一个整数："))
print(f"{num}不在10-20之间：",num>=10 or num<=20 )
