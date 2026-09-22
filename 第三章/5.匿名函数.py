#匿名函数
#需求1:打印一个分割线
out_line=lambda :print("------------------------")
out_line()

#需求2:计算两个数的和
add=lambda a,b:a+b
print(add(1,2))

#需求三:完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序
data_list=["C++","python","java","C","javascript"]
print(data_list)

data_list.sort(key=lambda item:len(item),reverse=True)#匿名函数典型的应用场景,
print(data_list)
