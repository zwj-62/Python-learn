# # 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# # 5. 列出所有学生：遍历所有学生信息并输出。
# # 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# # 7. 退出系统
#
# student_dict={}
# print("欢迎进入教务管理系统~")
# while True:
#     menu = """
#     ###############################################################################################
#     #                                                                                             #
#     #1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统  #
#     #                                                                                              #
#     ################################################################################################
#     """
#     print(menu)
#     choice=int(input("请输入您需要进行的操作（1-7）："))
#     match choice:
#         case 1:
#             student_name=input("请输入要添加学生的姓名：")
#             if student_name in student_dict:
#                 print("该学生已经存在，请重新选择操作：")
#                 continue
#             chinese_score=int(input("请输入该学生的语文成绩："))
#             math_score=int(input("请输入该学生的数学成绩："))
#             english_score=int(input("请输入该学生的英语成绩："))
#             student_dict[student_name]={"chinese_score":chinese_score,"math_score":math_score,"english_score":english_score}
#             print("添加学生信息成功~")
#         case 2:
#             student_name=input("请输入要修改学生的姓名：")
#             if student_name not in student_dict:
#                 print("该学生不存在，请重新选择操作：")
#                 continue
#             chinese_score=int(input("请输入该学生的语文成绩："))
#             math_score=int(input("请输入该学生的数学成绩："))
#             english_score=int(input("请输入该学生的英语成绩："))
#             student_dict[student_name]={"chinese_score":chinese_score,"math_score":math_score,"english_score":english_score}
#             print("修改学生信息成功~")
#         case 3:
#             student_name=input("请输入要删除学生的姓名：")
#             if student_name not in student_dict:
#                 print("该学生不存在，请重新选择操作：")
#                 continue
#             del student_dict[student_name]
#             print("删除学生信息成功")
#         case 4:
#             student_name=input("请输入要查询的学生姓名：")
#             if student_name not in student_dict:
#                 print("查询的学生姓名不存在，请重新选择")
#                 continue
#             print(student_dict[student_name])
#         case 5:
#             for student_name in student_dict.keys():
#                 student_info = student_dict[student_name]
#                 print(f"学生姓名{student_name},语文成绩：{student_info['chinese_score']},数学成绩：{student_info['math_score']},英语成绩{student_info['english_score']}")
#         case 6:
#             if not student_dict:
#                 print("暂时没有学生信息，无法进行统计")
#                 continue
#             #新定义list列表，然后放入成绩
#             chinese_scores=[]
#             math_scores=[]
#             english_scores=[]
#             for name,info in student_dict.items():
#                 #把成绩和姓名形成一个元组，然后将这个元组放到列表中
#                 chinese_scores.append((info['chinese_score',name]))
#                 math_scores.append((info['math_score',name]))
#                 english_scores.append((info['english_score',name]))
#             #使用max/min函数，按成绩最高分和最低分并使用sum和len计算平均分
#             chinese_max=max(chinese_scores)
#             chinese_min=min(chinese_scores)
#             chinese_avg=sum(chinese_scores)/len(chinese_scores)
#             math_max=max(math_scores)
#             math_min=min(math_scores)
#             math_avg=sum(math_scores)/len(math_scores)
#             english_max=max(english_scores)
#             english_min=min(english_scores)
#             english_avg=sum(english_scores)/len(english_scores)
#             print("############班级成绩统计#############")
#             # 分别输出分数 + 对应学生姓名
#             print(f"语文最高分：{chinese_max[0]}（{chinese_max[1]}）,语文最低分：{chinese_min[0]}（{chinese_min[1]}）,语文平均分：{chinese_avg:.2f}")
#             print(
#                 f"数学最高分：{math_max[0]}（{math_max[1]}）,数学最低分：{math_min[0]}（{math_min[1]}）,数学平均分：{math_avg:.2f}")
#             print(
#                 f"英语最高分：{english_max[0]}（{english_max[1]}）,英语最低分：{english_min[0]}（{english_min[1]}）,英语平均分：{english_avg:.2f}")
#         case 7:
#             break


# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5. 列出所有学生：遍历所有学生信息并输出。
# 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7. 退出系统

student_dict = {}
print("欢迎进入教务管理系统~")
while True:
    menu = """
    ###############################################################################################
    #                                                                                             #
    #1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统  #
    #                                                                                              #
    ################################################################################################
    """
    print(menu)
    choice = int(input("请输入您需要进行的操作（1-7）："))
    match choice:
        case 1:
            student_name = input("请输入要添加学生的姓名：")
            if student_name in student_dict:
                print("该学生已经存在，请重新选择操作：")
                continue
            chinese_score = int(input("请输入该学生的语文成绩："))
            math_score = int(input("请输入该学生的数学成绩："))
            english_score = int(input("请输入该学生的英语成绩："))
            student_dict[student_name] = {"chinese_score": chinese_score, "math_score": math_score,
                                          "english_score": english_score}
            print("添加学生信息成功~")
        case 2:
            student_name = input("请输入要修改学生的姓名：")
            if student_name not in student_dict:
                print("该学生不存在，请重新选择操作：")
                continue
            chinese_score = int(input("请输入该学生的语文成绩："))
            math_score = int(input("请输入该学生的数学成绩："))
            english_score = int(input("请输入该学生的英语成绩："))
            student_dict[student_name] = {"chinese_score": chinese_score, "math_score": math_score,
                                          "english_score": english_score}
            print("修改学生信息成功~")
        case 3:
            student_name = input("请输入要删除学生的姓名：")
            if student_name not in student_dict:
                print("该学生不存在，请重新选择操作：")
                continue
            del student_dict[student_name]
            print("删除学生信息成功")
        case 4:
            student_name = input("请输入要查询的学生姓名：")
            if student_name not in student_dict:
                print("查询的学生姓名不存在，请重新选择")
                continue
            print(student_dict[student_name])
        case 5:
            for student_name in student_dict.keys():
                student_info = student_dict[student_name]
                print(
                    f"学生姓名{student_name},语文成绩：{student_info['chinese_score']},数学成绩：{student_info['math_score']},英语成绩{student_info['english_score']}")
        case 6:
            if not student_dict:
                print("暂时没有学生信息，无法进行统计")
                continue
            # 新定义list列表，然后放入成绩
            chinese_scores = []
            math_scores = []
            english_scores = []
            for name, info in student_dict.items():
                # 修复：取出成绩，和姓名组合为元组存入列表
                chinese_scores.append((info['chinese_score'], name))
                math_scores.append((info['math_score'], name))
                english_scores.append((info['english_score'], name))
            # 使用max/min获取最值元组，提取分数计算平均分
            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(s for s, n in chinese_scores) / len(chinese_scores)

            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(s for s, n in math_scores) / len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(s for s, n in english_scores) / len(english_scores)

            print("############班级成绩统计#############")
            # 分别输出分数 + 对应学生姓名
            print(
                f"语文最高分：{chinese_max[0]}（{chinese_max[1]}）,语文最低分：{chinese_min[0]}（{chinese_min[1]}）,语文平均分：{chinese_avg:.2f}")
            print(
                f"数学最高分：{math_max[0]}（{math_max[1]}）,数学最低分：{math_min[0]}（{math_min[1]}）,数学平均分：{math_avg:.2f}")
            print(
                f"英语最高分：{english_max[0]}（{english_max[1]}）,英语最低分：{english_min[0]}（{english_min[1]}）,英语平均分：{english_avg:.2f}")
        case 7:
            break
        case _:
            print("输入错误，请从新修改")