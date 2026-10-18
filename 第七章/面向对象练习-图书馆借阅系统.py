# 练习二：基于面向对象实现可保存、可恢复的图书借阅管理系统
# 某社区图书馆需要开发一个简单的图书借阅管理系统。系统支持图书查询、会员查询、借书、还书、查看借阅记录，以及数据保存和恢复。
# 系统中有普通会员和 VIP 会员，两种会员的借阅额度不同。请使用面向对象的编程思想完成系统开发，通过会员编号进行借阅操作。
# 核心功能：
# 1. 查看图书：展示图书编号、书名、作者、分类、价格、总数量和当前可借数量。
# 2. 查询会员：根据会员编号，查询会员姓名、会员类型、最大借阅数量及当前未归还数量。
# 3. 借书：根据会员编号和图书编号借出一本书。借阅成功后，减少对应库存，并生成唯一的借阅编号。
# 4. 还书：根据借阅编号归还图书。归还成功后，增加对应库存，并将借阅记录标记为已归还。
# 5. 查看会员借阅：根据会员编号，展示该会员尚未归还的借阅记录，包括借阅编号和图书编号。
# 6. 保存数据：将图书、会员和借阅记录保存到项目中的状态文件。
# 7. 恢复数据：重新运行程序后，恢复之前的库存和借阅状态；第一次运行、没有状态文件时，才使用样例数据初始化。
# 借阅规则：
# 1. 普通会员最多同时借阅 3 本。
# 2. VIP 会员最多同时借阅 6 + VIP等级 本。样例中的 V001 等级为 1，最多借 7 本。
# 3. 借阅额度只统计尚未归还的图书数量，已经归还的不再占用额度。
# 4. 图书没有可借库存，或者会员已达到借阅上限时，不能继续借书。
# 5. 每次借阅只借出一本。同一会员可以多次借同一种书，但每次都占用一本库存和一个借阅额度。
# 6. 每次成功借阅必须生成独立的借阅编号，保存和重启后也不能出现编号重复。
# 7. 只有存在且尚未归还的借阅记录可以归还。重复归还不能再次增加库存。
# 8. 每种图书始终满足：0 ≤ 可借数量 ≤ 总数量: 可借数量 + 尚未归还数量 = 总数量
#创建图书类
from abc import ABC ,abstractmethod
import json
import uuid

class Book:
    def __init__(self,book_id,title,author,category,price,total_number):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.price = price
        self.total_number = total_number
        self.available_number = total_number


#创建会员类
class Member(ABC):
    def __init__(self,member_id,member_name):
        self.member_id=member_id
        self.member_name=member_name

    #抽象类：获取最大阅读数量
    @abstractmethod
    def get_max_books(self):
        pass

#创建普通会员类
class NormalMember(Member):
    def get_max_books(self):
        return 3

#创建VIP会员类,继承Member
class VIPMember(Member):
    def __init__(self,member_id,member_name,vip_level   ):
        super().__init__(member_id, member_name)    #调用父类的构造方法
        self.vip_level = vip_level
    #抽象类：获取最大阅读数量
    def get_max_books(self):
        return 6 + self.vip_level



#创建借阅管理类，包含图书、会员和借阅记录，以及相关操作
class Library:
    def __init__(self):
        self.books = {}#图书字典
        self.members = {}#会员字典
        self.loans = {}#借阅字典

    #把图书放在图书馆中
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"图书 {book.title} 已添加到图书馆")
        pass

    #把会员保存在图书馆里
    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"会员 {member.member_name} 已添加到图书馆")
        pass

    #加载样例数据
    def load_initial_data(self, file_path):
        with open(file_path , 'r', encoding='utf-8') as f:
            data = json.load(f)
            for book_data in data['books']:
                book = Book(book_data['book_id'], book_data['title'], book_data['author'], book_data['category'],
                            book_data['price'], book_data['total_number'])
                self.add_book(book)
            for member_data in data['members']:
                member_id = member_data['member_id']

                if member_id.startswith('N'):
                    member = NormalMember(member_id, member_data['name'])
                elif member_id.startswith('V'):
                    member = VIPMember(
                        member_id,
                        member_data['name'],
                        member_data['vip_level']
                    )
                else:
                    raise ValueError(f'无法识别会员类型：{member_id}')

                self.add_member(member)
        print(f"数据已从 借阅系统样例数据.json 加载到图书馆")
        pass

    #查询图书
    def get_book(self, book_id):
        if book_id not in self.books:
            raise ValueError(f'图书编号不存在：{book_id}')

        return self.books[book_id]

    #查询会员
    def get_member(self, member_id):
        if member_id not in self.members:
            raise ValueError(f'会员编号不存在：{member_id}')

        return self.members[member_id]

    #查询会员尚未归还的记录
    def get_member_loans(self,member_id):
       #先确认会员是存在的，不存在的会报错
        self.get_member(member_id)
        #用列表收集符合的记录
        result=[]
        #self.loans 的值都是一条借阅记录
        for record in self.loans.values():
            if record['member_id'] == member_id and not record['returned']:
                result.append(record.copy())
        #遍历完之后，返回结果
        return result

    #实现借书
    def borrow_book(self, member_id, book_id):
        member = self.get_member(member_id)
        book = self.get_book(book_id)
        #获取这个会员的尚未归还记录
        current_loans=self.get_member_loans(member_id)
        #检查会员的额度
        if len(current_loans) >= member.get_max_books():
            print(f"会员 {member.member_name} 的借书额度已经满了，无法借阅图书 {book.title}")
            raise ValueError("会员的借书额度已经满了，无法借阅图书")
        #检查图书馆的图书库存
        if book.available_number<=0:
            print(f"图书 {book.title} 的库存已经没有了，无法借阅")
            raise ValueError("图书的库存已经没有了，无法借阅")
        #检查过后，为本次借阅图书生成新的独立编号
        loan_id = str(uuid.uuid4())
        #将借阅记录保存在字典中，借阅编号作为键值，保存完整记录
        self.loans[loan_id] = {
            'loan_id': loan_id,
            'member_id': member_id,
            'book_id': book_id,
            'returned': False
        }
        #借出去一本书
        book.available_number -= 1
        print(f"会员 {member.member_name} 已借阅图书 {book.title}")
        return loan_id

    #归还图书
    def return_book(self, loan_id):
        #检查借阅编号是否存在
        if loan_id not in self.loans:
            raise ValueError(f'借阅编号不存在：{loan_id}')
        #取数记录，检查是否已经归还
        record=self.loans[loan_id]
        if  record['returned'] == True:
            raise ValueError(f'借阅编号已经归还：{loan_id}')
        #找到对应的图书，查询库存上限
        book = self.get_book(record['book_id'])
        if book.available_number >= book.total_number:
            raise ValueError(f'图书 {book.title} 的库存已经满了，无法归还')
        #全部通过检查后，更新状态
        record['returned'] = True
        book.available_number += 1
        print(f"会员 {record['member_id']} 已归还图书 {record['book_id']}")
        return record.copy()
    #保存状态
    def save_state(self, file_path):
        books_data = []

        for book in self.books.values():
            book_data = {
                'book_id': book.book_id,
                'title': book.title,
                'author': book.author,
                'category': book.category,
                'price': book.price,
                'total_number': book.total_number,
                'available_number': book.available_number
            }

            books_data.append(book_data)

        # 先看看整理出来的数据
        # 整理会员信息
        members_data = []

        for member in self.members.values():
            vip_level = 0

            if isinstance(member, VIPMember):
                vip_level = member.vip_level

            member_data = {
                'member_id': member.member_id,
                'name': member.member_name,
                'vip_level': vip_level
            }

            members_data.append(member_data)

        # 将三组数据放进同一个字典
        state = {
            'books': books_data,
            'members': members_data,
            'loans': list(self.loans.values())
        }

        # 把整理好的数据写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=4)

        print('状态已保存到：', file_path)
#主函数
if __name__ == '__main__':
        library = Library()

        library.load_initial_data(
            r'D:\APP\python\python-test\Python\第七章\data_2\借阅系统样例数据.json'
        )

        # 借一本，制造一个需要保存的状态
        loan_id = library.borrow_book('N001', 'B001')

        # 保存当前状态
        library.save_state(
            r'D:\APP\python\python-test\Python\第七章\data_2\state.json'
        )
