# #函数定义
# # 注意：函数在定义的时候并不会执行，只有在函数调用的时候才会执行，必须先定义后调用
# def out_line():
#     print("--------------")
#     print("--------------")
#     print("--------------")

# #函数调用
# out_line()
# #函数每调用一次就执行一次
# out_line()
import math


# #函数的参数与返回值
# #函数1：计算圆的面积
# def circle_area(r):
#     area=3.1 * r**2
#     return area
# print(circle_area(5))
#
# #函数2：计算长方形的面积’
# def rectangle_area(l,w):
#     """
#     根据长方形的长度和宽度，计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area=l*w
#     return area
# #help(rectangle_area) 可以查看函数的说明文档
# print(rectangle_area(4,5))
#
#
# #函数3：计算圆的面积以及周长--------->如果返回值有多个，则在return后使用逗号分隔开----------->多个返回值会自动返回元组之中
# def circle_area_len(r):
#     """
#     根据圆的半径，计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 返回圆的面积和周长
#     """
#     area=3.14*r**2
#     len=2*3.14*r
#     return area,len
# al=circle_area_len(5)
# print(al)
# print(type(al))
# area,len=circle_area_len(4)
# print(area)
# print(len)
#



# #函数的嵌套使用  先进先出   也就是：a b c b a 这个流程
# def functiona():
#     print("a......before")
#     functionb()
#     print("a......after")
#
# def functionb():
#     print("b......before")
#     functionc()
#     print("b......after")
# def functionc():
#     print("c......before")
#
#
#
# functiona()
# print("函数调用完毕")

# #案例一：传入地和高然后计算三角形面积
# def triangle_area(b,h):
#     """
#     根据传入的地和高计算三角形的面积
#     :param b: 底
#     :param h: 高
#     :return: 返回面积
#     """
#     area = (b*h)/2
#     return area
# print("底长为30，高度为20的三角形的面积为：",triangle_area(30,20))
#
#
# #案例二：定义一个函数：计算传入的字符串中元音音节的个数
# def count_aeiou(s):
#     count = 0
#     for w in s:
#         if w in "aeiouAEIOU":
#             count += 1
#     return count
# count=count_aeiou("hello-python")
# print(count)
#
#
#
# #案例三：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分，最低分和平均分（保留一位小数），并返回
# def calc_score(score_list):
#     max_s=max(score_list)
#     min_s=min(score_list)
#     avg=round(sum(score_list)/len(score_list),1)#保留一位小数
#     return max_s,min_s,avg
# s_list=[437,242,432,644,706,231]
# max_s,min_s,avg=calc_score(s_list)
# print(max_s,min_s,avg)


# #作业一：定义一个函数，根据传入的分数，计算对应的分数等级并返回
# # 分数>=90：A
# # 分数>=75：B
# # 分数>=60:C
# # 分数<60:D
# def grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
# score=int(input("请输入分数："))
# print(f"该分数对应的等级是：{grade(score)}")


# #作业二：定义一个函数：用于判断一个字符串是否是回文串，并返回bool值
# def palindrome(str):
#     """
#     用于判断是否是回文串，然后返回布尔值
#     :param str: 传入字符串
#     :return: 返回布尔值
#     """
#     return str==str[::-1]
# s=input("请输入您要判断的字符串:")
# print(f"输入的字符串是否是布尔值：{palindrome(s)}")

#作业三：定义一个函数：完成时间转换功能，将传入的秒转换为小时，分钟，秒
def time_change(s):
    h=0
    m=0
    h=s//3600
    m=(s%3600)//60
    s=s%60
    return h,m,s
second=int(input("请输入要转换的秒："))
hour,minute,second=time_change(second)
print(f"转换后的时间为{hour}时{minute}分{second}秒")
