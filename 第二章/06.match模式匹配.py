# day=int(input("请输入星期几（1-7）："))
# match day:
#     case 1:
#         print("今天星期一：工作会议日")
#     case 2:
#         print("今天星期二：学习培训日")
#     case 3:
#         print("今天星期三：项目开发日")
#     case 4:
#         print("今天星期四：代码审查日")
#     case 5:
#         print("今天星期五：总结规划日")
#     case 6|7:
#         print("今天周末，休息日")
#     case _:
#         print("输入错误")



# #案例：基于match case 实现一个简单的计算器
# num1=float(input("请输入第一个数："))
# num2=float(input("请输入第二个数："))
# oper =input("请输入运算符（+ - * /）：")
# match oper:
#     case "+":
#         print("num1+num2=",num1+num2)
#     case "-":
#         print("num1-num2=",num1-num2)
#     case "*":
#         print("num1*num2=",num1*num2)
#     case "/" if num2!=0:
#         print("num1/num2=",num1/num2)
#     case _:
#         print("运算操作错误")




#简单游戏指令系统的开发
oper=input("请输入想要操作的指令：")
match oper:
    case "上"|"w"|"W":
        print("角色向上移动")
    case "下"|"s"|"S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"|" ":
        print("角色跳动")
    case "攻击"|"j"|"J":
        print("角色发起攻击")
    case "退出"|"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("输入指令错误")