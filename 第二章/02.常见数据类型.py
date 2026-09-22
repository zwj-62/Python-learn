#常见数据类型
print("hello")
print(type("hello"))

print(type(10))#int
print(type(3.14))#float
print(type(True))#bool
print(type(False))#bool
print(type(None))#Nonetype

num=-100
print(type(num))#int

#isinstance(数据，类型）是个bool类型的值，判定是否是指定类型
num=5.0
print(num)
print(isinstance(num,float))
print(isinstance(num,int))
print(isinstance(num,bool))


#字符串
#字符串的三种定义方式
s1="hello"#双引号定义方式
s2='hello'#单引号定义方式
s3="""
hello;
    欢迎大家进入到python课程的学习
    大家记得一键三连哦~
    """#这是三引号的定义方式
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))

#定义字符串----->It's very good
msg1="It's very good"
print(msg1)

msg2='It\'s very good'
print(msg2)

msg3='hello的意思是“您好"'
print(msg3)

mgs4="hello的意思是\“您好\""
print(mgs4)

print("\t欢迎大家进入python课程的学习！\n\t大家记得一键三连哦~")







#字符串的拼接
s1="人生苦短""我用python"",ok"
print(s1)

msg1="人生苦短"
msg2="我用python"
print("鬼叔说："+msg1+","+msg2)

#案例----->str(int数字)将int类型的数据转为字符串类型
name="涛哥"
age=18
pro="软件工程"
hobby="python、java"
print("大家好，我是"+name+",今年"+str(age)+"岁，我学习的专业是"+pro+"，我的热爱是"+hobby)




#字符串格式化---->方式一
name="涛哥"
age=18
pro="软件工程"
hobby="python、java"
print("大家好，我是%s,今年%s岁，我学习的专业是%s，我的热爱是%s"%(name,age,pro,hobby))

#字符串格式化---->方式二，企业推荐使用方式
name="涛哥"
age=18
pro="软件工程"
hobby="python、java"
print(f"大家好，我的名字是{name},我的年龄是{age},我的专业是{pro},我的爱好是{hobby}")