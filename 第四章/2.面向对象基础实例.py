# 案例：采用面向对象编程思想完成教务管理系统开发
# 需求说明：通过控制台菜单与用户交互，管理在校学生成绩信息
# 功能1：添加学生成绩
# 根据输入的学生姓名、语文成绩、数学成绩、英语成绩，创建学生对象记录到系统中
# 功能2：修改学生成绩
# 根据输入的学生姓名，匹配对应学生并更新三科成绩
# 功能3：删除学生成绩
# 根据输入的学生姓名，找到对应学生并从系统中移除
# 功能4：查询指定学生成绩
# 根据输入的学生姓名检索学生，输出该学生完整成绩信息
# 功能5：展示全部学生成绩
# 遍历系统内所有学生，统一展示全部学生的成绩数据

#学生类
class Student:
    def __init__(self,name,chinese,math,english):#需要传入参数的形参
        #属性名称
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    #输出学生信息：
    def __str__(self):
        return f"姓名:{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}|总分：{self.chinese+self.math+self.english}"
    #修改学生的成绩
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None :
            self.chinese=chinese
        if math is not None :
            self.math=math
        if english is not None :
            self.english=english

#测试学生类
if __name__=="__main__":
    s1=Student("王琳",90,88,91)
    print(s1)
    s1.update_score(english=95)
    print(s1)

#教务管理系统的类
class EduManagement:
    system_version="1.0"
    system_name="教务管理系统"
    def __init__(self):
        self.student_list=[]#列表，记录的是在校学生的管理信息

    #添加学生成绩
    def add_student(self):
        name=input("请输入学生的姓名：")
        for s in self.student_list:
            if s.name==name:
                print("该学生已经存在，添加失败")
                return #直接结束代码
        chinese=int(input("请输入该学生的语文成绩："))
        #判断分数是否在0-100之间
        if chinese<0 or chinese>100:
            print("语文成绩不在有效范围内，添加失败")
            return
        math=int(input("请输入该学生的数学成绩："))
        if math<0 or math>100:
            print("数学成绩不在有效范围内，添加失败")
            return
        english=int(input("请输入该学生的英语成绩："))
        if english<0 or english>100:
            print("英语成绩不在有效范围内，添加失败")
            return
        stu=Student(name,chinese,math,english)
        self.student_list.append(stu)
        print("添加学生成功")

    #修改学生成绩
    def update_score(self):
        name=input("请输入需要修改的学生姓名：")
        for s in self.student_list:
            if s.name==name:
                print(f"当前成绩：{s}")
                chinese=int(input("请输入修改后的语文成绩："))
                math=int(input("请输入修改后的数学成绩："))
                english=int(input("请输入修改后的英语成绩："))
                #判断输入的成绩是否在有效范围内
                if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                    s.update_score(chinese=chinese, math=math, english=english)
                    print(f"修改后的成绩：{s}")
                else:
                    print("修改的成绩不在有效范围内，必须在0-100之间")
                return
        print("未找到该学生，修改失败")

    # 删除学生成绩
    def delete_score(self):
        name=input("请输入要删除学生的姓名：")
        for s in self.student_list:
            if s.name==name:
               self.student_list.remove(s)
               print("删除学生信息成功")
               return
        print("未找到该学生，删除失败")

    # 查询指定学生成绩
    def query_score(self):
        name=input("请输入需要查询的学生姓名：")
        for s in self.student_list:
            if s.name==name:
                print(f"查询的学生信息为：{s}")
                return
        print("未查询到该学生")

    # 展示全部学生成绩
    def list_student(self):
        if not self.student_list:
            print("暂无学生信息")
            return
        for s in self.student_list:
            print(s)

    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统V{EduManagement.system_version}")
        while True:
            print()
            print("###############################################################")
            print("1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统")
            print("###############################################################")
            choice=int(input("请选择要执行的操作：1-6："))
            match choice:
                case 1:
                    self.add_student()
                case 2:
                    self.update_score()
                case 3:
                    self.delete_score()
                case 4:
                    self.query_score()
                case 5:
                    self.list_student()
                case 6:
                    print("退出系统，拜拜~")
                    break
                case _:
                    print("输入错误，请选择1-6之间的菜单功能")

#测试
if __name__=="__main__":
    edumanagement=EduManagement()
    edumanagement.run()