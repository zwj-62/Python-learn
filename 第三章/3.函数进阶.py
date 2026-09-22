# #------------------------------函数-不定长参数（位置参数*args）-------------------------
# #需求：根据传入的这批数据，计算这批数据的最大值，最小值，平均值
# def calc_data(*args):
#     max_data=max(args)
#     min_data=min(args)
#     avg_data=round(sum(args)/len(args),1)
#     return max_data,min_data,avg_data
# #调用函数
# print(calc_data(1,2,3,4,5,6,7,8,9))
# print(calc_data(32,53,64,22,55,85,566,908,78,34))

#-------
#------------------------------函数-不定长参数（关键字传递的不定长参数**kwargs）-------------------------
#传入的不定长参数会被合并封装为一个字典类型的参数
def calc_data(*args,**kwargs):
    """
    根据传入的参数,计算这批数据的最大值,最小值,平均值
    :param args: 不定长位置参数
    :param kwargs: 不定长关键字参数
    :return: 返回最大值最小值平均值
    """
    max_data=max(args)
    min_data=min(args)
    avg_data=sum(args)/len(args)
    print(kwargs)
    if kwargs.get("round")is not None:
       avg_data=round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出来的最小值是:{min_data},最大值是:{max_data},平均值是:{avg_data}")
    return max_data,min_data,avg_data
#调用函数
print(calc_data(1,2,3,4,5,6,7,8,9,round=3))
print(calc_data(32,53,64,22,55,85,566,908,78,34,round=2,print=True))
