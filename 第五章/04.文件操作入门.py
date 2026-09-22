# #读文件
# #1.打开文件
# from openai.resources.skills.versions import content
#
# f=open("./resources/望庐山瀑布.txt","r",encoding="utf-8")
# #2.读取文件
# content=f.read()#读取所有文件
# print(content )
#
# #3.关闭文件
# f.close()
#====================================================================
#写文件
#1.打开文件
#方式一：
# f=open("./resources/静夜思.txt","w",encoding="utf-8")
#
# try:
#     f.write("床前明月光")
#     f.write("疑是地上霜")
#     f.write("举头望明月")
#     f.write("低头思故乡")
# except Exception as e:
#     print(e)
# finally:
#     f.close()


#方式二：是项目开发的推荐方式
with open("./resources/静夜思.txt","w",encoding="utf-8") as f:
    f.write("床前明月光")
    f.write("疑是地上霜")

    f.write("举头望明月")
    f.write("低头思故乡")
    f.close()
