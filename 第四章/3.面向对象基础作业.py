# 采用面向对象编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物车


#商品goods类
class goods:
    def __init__(self,name,price,num):
        #属性名称
        self.name=name
        self.price=price
        self.num=num
    #输出商品信息
    def __str__(self):
        return f'商品名称：{self.name},商品价格：{self.price},商品数量：{self.num}'
    #修改商品信息
    def update(self,price=9.9,num=100):
        self.price=price
        self.num=num
#测试goods类
if __name__=='__main__':
    g1=goods("矿泉水",2.0,200)
    print(g1)
    g1.update(price=9.9,num=400)
    print(g1)
#购物车管理系统的类
class ShoppingCart:
    system_version=1.0
    system_name="购物车管理系统"
    def __init__(self):
        self.goods_list=[]#列表，用于记录购物车中物品的信息
    #添加商品信息
    def add_good(self):
        name=input("请输入要添加的商品的名称：")
        for s in self.goods_list:
            if s.name==name:
                print("该商品已经存在，添加失败")
                return
        price=float(input("请输入添加商品的价格："))
        if price<=0:
            print("输入的商品的价格不合理")
            return
        num=int(input("请输入添加商品的数量："))
        if num<=0:
            print("输入商品的数量不合理")
            return
        good=goods(name,price,num)
        self.goods_list.append(good)
        print("商品添加成功")
    #修改购物车
    def goods_update(self):
        name=input("请输入要修改商品的名字：")
        for s in self.goods_list:
            if s.name==name:
                print(f"当前商品信息：{s}")
                price=float(input("请输入要修改商品的价格："))
                if price<=0:
                    print("输入商品的价格不合理")
                    return
                num=int(input("请输入要修改商品的数量："))
                if num<=0:
                    print("输入商品的数量不合理")
                    return
                s.update(price=price,num=num)
                print("修改后的商品信息")
            print("该商品不存在")

    #删除购物车
    def goods_delete(self):
        name=input("请输入要删除的商品名称：")
        for s in self.goods_list:
            if s.name==name:
                self.goods_list.remove(s)
                print("删除商品成功")
                return
        print("未找到该商品，删除失败")
    #查询购物车
    def goods_show(self):
        if not self.goods_list:
            print("暂无商品信息")
            return
        for s in self.goods_list:
            print(s)
    #运行系统
    def run(self):
        print(f"欢迎使用购物车管理系统V{ShoppingCart.system_version}")
        while True:
            print()
            print("##################################################")
            print("1.添加商品 2.修改商品 3.删除商品 4.查询购物车 5.推出购物车")
            print("##################################################")
            try:
                choice=int(input("请选择要执行的操作（1-5）："))
                match choice:
                    case 1:
                        self.add_good()
                    case 2:
                        self.goods_update()
                    case 3:
                        self.goods_delete()
                    case 4:
                        self.goods_show()
                    case 5:
                        print("退出购物车系统")
                        break
                    case _:
                        print("输入的操作不正确，请重新输入")
            except ValueError as e:
                print("输入的数据有问题，请重新输入！！！！！")
            except Exception as e:
                print("程序运行出错")


#测试
if __name__=="__main__":
    shoppingcart=ShoppingCart()
    shoppingcart.run()


