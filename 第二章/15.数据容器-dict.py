# #字典
# #定义字典--------->字典中的key是不能重复的，如果重复了，则会被覆盖，所以key必须是不可变类型的（str,int float,tuple)
# dict1={"王琳":670,"李沐晚":608,"徐立国":688,"庄雯静":701}
# print(dict1)
# print(type(dict1))
#
# dict2={0:670,1:608,2:688,3:701,('A','B'):666}
# print(dict2)
#
# #访问：只会访问，不会被修改key，但是value可以被修改
# print(dict1["李沐晚"])
# dict1["李沐晚"]=688
# print(dict1)
#
# #添加修改-key不存在的时候是添加，存在则是修改
# dict1["涛哥"]=330
# print(dict1)
#
# #查询 根据key查询value
# print(dict1["涛哥"])
# print(dict1.get("涛哥"))
#
#
# print(dict1.keys())#获取所有的key
# print(dict1.values())#获取所有的value
# print(dict1.items())#获取所有的项目
#
# #删除------>删除是有返回值的
# score=dict1.pop("徐立国")
# print(score)
# print(dict1)
#
# #del删除操作
# del dict1["王琳"]
# print(dict1)
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# for item in dict1.items():#每个dict都有两个量，统一给item 然后再从item中输出
#     print(f"{item[0]}: {item[1]}")





#案例--------------购物车管理系统，实现商品信息添加，修改，删除，查询的功能-------------
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物车

#制作菜单
# print("################购物车系统#################")
# print("#\t\t\t\t1.添加购物车\t\t\t\t#")
# print("#\t\t\t\t2.修改购物车\t\t\t\t#")
# print("#\t\t\t\t3.删除购物车\t\t\t\t#")
# print("#\t\t\t\t4.查询购物车\t\t\t\t#")
# print("#\t\t\t\t5.退出购物车\t\t\t\t#")
# print("################购物车系统#################")
shopping_cart={}
menu="""
############购物车系统##############
#          1.添加购物车            #  
#          2.修改购物车            #
#          3.删除购物车            #
#          4.查询购物车            #
#          5.退出购物车            #
##################################
"""
print(menu)
print("欢迎使用购物车管理系统！")
#执行对应的操作
while(1):
    choice = int(input("请输入对应的操作：1-5："))
    match choice:
        case 1:  # 添加购物车
            goods_name = input("请输入商品名称:")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("轻松输入商品数量："))
            # 如果商品已经存在，则不执行操作
            if goods_name in shopping_cart:
                print("商品已经存在，请重新选择：")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕")
        case 2:  # 修改购物车
            goods_name = input("请输入商品名称:")
            # 如果商品已经存在，则不执行操作
            if goods_name not in shopping_cart:
                print("商品已经不存在，请重新选择：")
                continue
            goods_price = float(input("请输入商品最新价格："))
            goods_num = int(input("轻松输入商品最新数量："))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完毕")
        case 3:  # 删除购物车
            goods_name = input("请输入要删除的商品的名称：")
            if goods_name not in shopping_cart:
                print("商品不存在，请重新选择：")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")
        case 4:  # 查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格:{goods_info['price']},商品数量：{goods_info['num']}")
        case 5:  # 退出购物车
            print("拜拜")
            break
        case _:
            print("非法操作不支持")
