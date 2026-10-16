from abc import abstractmethod
import json

class Book:
    def __init__(self,book_id, title, author, price,total_number):
        self.book_id = book_id#书籍编号
        self.title = title#书名
        self.author = author#作者
        self.price = price#价格
        self.total_number = total_number#总数量
        self.__avaliable = total_number#可借阅数量

    #借书
    def borrow_book(self):
        if self.__avaliable > 0:
            self.__avaliable -= 1
            return True
        else:
            return False
    #还书
    def return_book(self):
        self.__avaliable += 1

    #获取可借阅数量
    def get_avaliable_number(self):
        return self.__avaliable


#会员类
class Member:
    def __init__(self,member_id, name, password):
        self.member_id = member_id#会员编号
        self.name = name#会员名
        self.__password = password#会员密码
        self.__borrowed_books = []#借阅的书籍列表

    #借阅图书
    def borrowed_Book(self, book):
        #判断是否超过最大借书数量
        if len(self.__borrowed_books) >=self.get_max_books():
            print(f'借阅失败，你已经超过借阅数量，最多可借阅{self.get_max_books()}本书')
            return False
        #判断书籍是否可以被借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)#将书籍添加到借阅列表
            print(f'{self.name}借阅成功{book.title}，你已经借阅了{len(self.__borrowed_books)}本书')
            return True
        else:
            print(f'借阅失败，《{book.title}》已借阅完毕')
            return False


    #还书
    def return_book(self, book):
        #判断书籍是否在借阅列表中
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
            print(f'{self.name}还书成功《{book.title}》')
            return True
        else:
            print(f'还书失败，你没有借阅过《{book.title}》')
            return False

    #获取会员密码
    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books
    #获取最大可以借书的数量
    #抽象方法必须在子类中实现
    @abstractmethod
    def __get_max_books(self):
        pass

#普通会员
class NormalMember(Member):
    #抽象方法在子类中
    def get_max_books(self)->int:
        return 3


#VIP会员
class VipMember(Member):
    def __init__(self, member_id, name, password, vip_lever):
        super().__init__(member_id, name, password)
        self.vip_lever = vip_lever
    #抽象方法在子类中
    def get_max_books(self)->int:
        return 6+self.vip_lever#会员等级


#图书馆管理系统
class LibrarySystem:
    def __init__(self):
        self.books ={}#用字典可以快速查找书籍例如{“AI001”:Book对象，“AI002”:Book对象}
        self.members={}#会员字典--------》{“N001”:Member对象，"N002”:Member对象}
        self.current_member:Member|None#当前登录的会员对象，如果没有则为None\
        #加载输入书籍信息
        self.load_books_data()
        #加载输入会员信息
        self.load_members_data()

    def load_books_data(self):
        #加载data/book.josn 文件中的数据
        with open('data/books.json', 'r', encoding='utf-8') as f:
            books_data = json.load(f)
            for book_data in books_data:
                # 注意：books.json 里的键是中文（编号/标题/作者/数量），必须用中文键取值，用英文键会报 KeyError
                # JSON 中没有"价格"字段，这里用 get('价格', 0) 给默认价 0；以后给 JSON 补上价格字段后这里能自动读到
                book = Book(book_data['编号'], book_data['标题'], book_data['作者'], book_data.get('价格', 0), book_data['数量'])
                self.books[book_data['编号']] = book  # 字典的键也要用中文键'编号'，和上面保持一致
            print("书籍加载成功")

    def load_members_data(self):
        #加载data/members.json 文件中的数据
        with open('data/members.json', 'r', encoding='utf-8') as f:
            members_data = json.load(f)
            for member_data in members_data:
                # members.json 里的键是中文：卡号/姓名/密码/会员等级
                # 卡号以 N 开头 → 普通会员；以 V 开头 → VIP会员（需要额外传"会员等级"）
                if member_data['卡号'].startswith('N'):
                    member = NormalMember(member_data['卡号'], member_data['姓名'], member_data['密码'])
                elif member_data['卡号'].startswith('V'):
                    member = VipMember(member_data['卡号'], member_data['姓名'], member_data['密码'], member_data['会员等级'])
                self.members[member_data['卡号']] = member
            print("会员加载成功")

    def login(self):
        while True:
            member_id = input('请输入会员编号：')
            password = input('请输入会员密码：')
            if member_id in self.members and self.members[member_id].get_password() == password:
                self.current_member = self.members[member_id]
                print(f'欢迎回来，{self.current_member.name}')
                return True
            else:
                print('会员编号或密码错误，请重新输入')
    def borrow_book(self ):
        #1:展示现在的图书馆图书列表
        for book_id,book in self.books.items():
            print(f"编号：{book_id}, 标题：{book.title}, 作者：{book.author}, 价格：{book.price}, 数量：{book.total_number}, 可借阅数量：{book.get_avaliable_number()}")
        #2：选择要借阅的图书
        book_id = input("请输入要借阅的图书编号：")
        if book_id not in self.books:
            print("无效的图书编号，请重新输入")
            return
        self.current_member.borrowed_Book(self.books[book_id])#借阅书籍

    def return_book(self):
        #1:展示目前会员已经借阅的图书
        for book in self.current_member.get_borrowed_books():
            print(f"编号：{book.book_id}, 标题：{book.title}, 作者：{book.author}, 价格：{book.price}, 数量：{book.total_number}, 可借阅数量：{book.get_avaliable_number()}")
        #2：选择要归还的图书
        book_id = input("请输入要归还的图书编号：")
        borrowed_ids=[book.book_id for book in self.current_member.get_borrowed_books()]
        if book_id not in borrowed_ids:
            print("无效的图书编号，请重新输入")
            return
        self.current_member.return_book(self.books[book_id])#归还书籍
    #3：查询借阅
    def show_borrowed_books(self):
        #1:展示目前会员已经借阅的图书
        for book in self.current_member.get_borrowed_books():
            print(f"编号：{book.book_id}, 标题：{book.title}, 作者：{book.author}, 价格：{book.price}, 数量：{book.total_number}, 可借阅数量：{book.get_avaliable_number()}")
    # 控制运行
    def run(self):
        if self.login():
            while True:
                print("\n1：借阅图书")
                print("2：归还图书")
                print("3：查询借阅")
                print("4：退出系统")
                choice = input("请输入你的选择：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统,Bye Bye")
                        return
                    case _:
                        print("无效的选择，请重新输入")

if __name__ == '__main__':
    ls=LibrarySystem()
    print(ls.books)
    print(ls.members)
    ls.run()

