"""
 案例：电商订单计算器
 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
 具体规则如下：
 1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
 2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def cal_order_cost(*args,coupon=0,score=0,express=0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
    :param args:商品信息（商品名称，价格，数量）-------->（“鼠标”，188，2）（“键盘”，388，1）
    :param coupon:优惠券
    :param score:积分抵扣
    :param express:订单总金额
    :return:
    """
    #订单总金额=商品总金额-优惠券-积分抵扣+运费
    #1.计算商品总金额
    total_price=[goods[1]*goods[2] for goods in args]#把每一个商品的总金额（数量*商品物价）都放在total_price list列表中
    total_cost=sum(total_price)#计算列表中所有商品的总金额
    #2.扣减优惠券
    if total_cost>=5000 and total_cost>=coupon:
        total_cost=total_cost-coupon

    #3.扣减积分抵扣
    if total_cost>=5000 and total_cost>=score//100:
        total_cost-=score//100
    #4.添加运费
    total_cost=total_cost+express
    return total_cost


#测试
num1=cal_order_cost(("鼠标",188,2),("矿泉水",2,5),("手机",5999,1),("电脑",7999,1),coupon=10,score=4000,express=9.9)
print(num1)
num2=cal_order_cost(("鼠标",188,2),("矿泉水",2,5),("手机",5999,1),("电脑",8999,1),coupon=500)
print(num2)
