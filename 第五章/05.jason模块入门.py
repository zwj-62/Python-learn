import json

from numpy.lib.recfunctions import flatten_descr

#写入json数据文件
user={
    "name":"张三",
    "age":18,
    "sex":"男",
    "hobbies":["看课","打游戏","听音乐"]
}
with open ("resources/user.json","w",encoding="utf-8") as f:
    # ensure_ascii=False,是默认为True 的，如果要输出中文，需要设置为false
    # indent=2,是默认为none 的，如果要输出格式化，需要设置为2
    json.dump(user,f,ensure_ascii=False,indent=2)


#读取json数据文件
with open ("resources/user.json","r",encoding="utf-8") as f:
    user=json.load(f)
    print(user)
    print(type(user))