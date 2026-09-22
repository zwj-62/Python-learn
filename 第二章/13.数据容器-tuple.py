# #元组基本操作-tuple
# #定义一个元组
# t1=(56,31,10,80,10,10,20)
# print(t1)
# print(type(t1))
#
# #索引查询
# print(t1[0])
# print(t1[-1])
#
# #元组的切片操作
# print(t1[0:5:1])
#
# #count()统计元素的个数
# print(t1.count(10))
#
# #index()获取元素的索引（第一个元素的位置）
# print(t1.index(10))
#
# #注意点
# t2=()
# print(t2)
# print(type(t2))
# #如果要表示单元素元组，表示元组要加一个，
# t3=(100,)
# print(t3)

# #组包和解包操作
# t1=(2,4,8,33,13,12)
# t2=2,4,8,33,13,12
# print(t1)
# print(t2)
#
# #解包操作
# #基础解包操作（变量数量和容器的元数个数一致）
# a,b,c,d,e,f,=t1
# print(a,b,c,d,e,f)
# #扩展解包，*可以收集剩余的所有元素，封装列表list中
# first,second,*other,last=t1
# print(first)
# print(second)
# print(other)
# print(last)
# *other,last2,last1=t1
# print(other)
# print(last2)
# print(last1)
# a=10
# b=20
# #使用组包和解包的思想
# a,b=b,a
# print(a,b)
# #a=100,b=200,c=300.a b c 分别赋值给 c a b
# a=100
# b=200
# c=300
# c,a,b=a,b,c
# print(a,b,c)


#案例：----------根据提供的学生成绩表，完成以下要求----------------
#           计算每个学生的总分，各科平均分，然后以并输出
#           统计各科的最高分，最低分，平均分，并输出
#           查找各科成绩优秀的学生，并输出
student=(
("S001","王林",85,92,78),
("S002","李沐",92,88,95),
("S003","十三",78,85,82),
("S004","曾就",88,79,91),
("S005","周铁",95,96,89),
("S006","红蝶",89,91,94),
("S007","徐国",75,82,77),
("S008","王卓",76,82,78),
("S009","许木",86,89,98),
("S010","小天",66,59,72),
)
# #          1、计算每个学生的总分，各科平均分，然后以并输出
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# for s in student:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     print(f"{s[0]}\t{s[1]} \t{s[2]}\t\t{s[3]}\t\t{s[4]} \t\t{total}\t\t{avg:.1f}")#avg:.1f 表示保留一位小数，并且是浮点数
# print("\n")
#方式二：使用解包操作实现
for id,name,chinese,math,english in student:
    total=chinese+math+english
    avg=total/3
    print(f"{id}\t{name} \t{chinese}\t\t{math}\t\t{english} \t\t{total}\t\t{avg:.1f}")
#           2、统计各科的最高分，最低分，平均分，并输出
Chinese_score=[s[2] for s in student]#直接在元组中提取元组的每一个元素中的第三个元素
print(f"语文最低分：{min(Chinese_score)}，最高分：{max(Chinese_score)}平均分：{sum(Chinese_score)/len(Chinese_score)}")
# Chinese_score.sort()
# print(Chinese_score[0])
Math_score=[s[3] for s in student]
print(Math_score)
print(f"数学最低分：{min(Math_score)},最高分：{max(Math_score)},平均分：{sum(Math_score)/len(Math_score)}")
English_score=[s[4] for s in student]
print(English_score)
print(f"英语最低分：{min(English_score)},最高分：{max(English_score)},平均分：{sum(English_score)/len(English_score)}")
print("\n")
#          3、 查找各科成绩优秀的学生，平均分大于九十并输出
for s in student:
    total=s[2]+s[3]+s[4]
    avg=total/3
    if avg>90:
        print(f"学号：{s[0]},姓名：{s[1]},平均分：{avg:.1f}")
