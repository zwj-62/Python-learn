# #集合-set------------->无序，不可重复
# #定义
# s1={3,4,6,7,2,76,8,32,3,56,78}
# print(s1)
# print(type(s1))
# #如果想要定义一个空集合，要使用set()
# s2={}
# print(type(s2))#输出字典类型
# s3=set()
# print(type(s3))


#
# #常见的方法
# #add()：添加元素到集合
# s1={1,2,3,4,5,6,7,8,9}
# s1.add(10)
# print(s1)
# #remove()：移除集合中的指定元素，指定元素不存在就会报错
# s1.remove(10)
# print(s1)
# #pop()：随机删除集合中的元素并返回
# e=s1.pop()
# print(e)
# print(s1)
# #clear():清空集合
# s1.clear()
# print(s1)#空集合的表示方式：set()
#
# s2={"A","B","C","D","E"}
# s3={"C","D","E","F","G","H"}
#
# #difference(),求两个集合的差集（存在于第一个集合，但是不存在于第二个集合
# print(s2.difference(s3))
# print(s3.difference(s2))
#
# #union()：求两个集合的并集
# print(s2.union(s3))
# print(s3.union(s2))#求s2 s3的并集，两个集合应该是一样的
#
# #intersection():求两个集合的交集
# print(s2.intersection(s3))
# print(s3.intersection(s2))#两个集合交集也应该一样


#------------------------集合set案例-----------------------
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王婵", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
#1.找出同时选修了法语和艺术的学生
#方式一：直接求交集
print(f"同时选修法语和艺术的学生：{french_set.intersection(art_set)}")
#方式二：&
print(f"同时选修法语与艺术的学生：{french_set&art_set}")

#找出同时选修了所有四门课程的学生
print(f"同时选修四门课课程的学生：{football_set&basketball_set&french_set&art_set}")

#找出选修了足球，但是没有选修篮球的学生
print(f"选修了足球但是没有选修篮球的学生：{football_set.difference(basketball_set)}")
#可以直接使用减号来实现求差集
print(f"选修了足球但是没有选修篮球的学生：{football_set-basketball_set}")
#集合推导式：{要往集合中添加的数据for s in set1 if 条件
ftball_set={s for s in football_set if s not in basketball_set}
print(f"选修了足球但是没有选修篮球的学生：{ftball_set}")

#统计每一个学生选修的课程数量
#获取到学生名单
allset1=football_set.union(basketball_set).union(french_set).union(art_set)
print(f"学生名单：{allset1}")
allset2=football_set|basketball_set|french_set|art_set
print(f"学生名单：{allset2}")
#获取每一个学生的课程数量
#解包
all_list=[*football_set,*basketball_set,*french_set,*art_set]
for s in all_list:
    print(f"{s}选修了{all_list.count(s)}")