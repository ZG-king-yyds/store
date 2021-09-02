import random
print("***************************************************")
print("*                   山海银行                        *")
print("***************************************************")
# print("                                                   ")
print("*1.开户                                           *")
print("*2.存钱                                           *")
print("*3.取钱                                           *")
print("*4.转账                                           *")
print("*5.查询                                           *")
print("*6.Bye！                                          *")
print("***************************************************")

bank={}#创建一个空的字典

#开户逻辑
bank_name="山海银行"
#                第一个对应第一个 不是名称对应名称

def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100:
        return 3
    if username in bank:#  如变量在容器内执行下面的代码
        return 2
    bank[username]={
        "account":account,#
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1
def adduser():#定义了一个方法
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    stast=bank_adduser(account,username,password,country,province,street,door)
    #        调用方法   （元素，，，，，，，，，）
    if stast == 3 :
        print("你去别的银行吧")
    elif stast== 2:
        print("用户名已存在")
    elif stast== 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))

#{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}


#存钱
def addmoney():
    while 1:
        username=input('请输入用户名:')
        password=input('请输入您的密码：')
        if username in bank:
            account  = input("请输入账号")
            print('您现在账户%s元' % (bank[username]['money']))
            a = input('请输入存款金额：')
            if a.isdigit():      #isdigit 判断是否是数字
                bank[username]['money'] +=int(a)
                print('尊敬的%s,存款已完成，您现在账户余额：%s' % (username, bank[username]['money']))
                print("您的个人信息如下所示")
                print("------------个人信息------------")
                print("用户名:%s" % (username))
                print("账号:%s" % (account))
                print("余额:%s" % (bank[username]['money']))
                print("开户行名称:%s" % (bank_name))
                print("------------山海银行-----------")
                break
        else:
            print("用户名不存在，请重新输入")
            return False


#取钱
def bank_quqian(username,password,account,c):
    if username not in bank:
        return 1
    elif bank[username]['password'] != password:
        return 2
    elif c.isdigit():
        bank[username]['money'] -= int(c)
        print('尊敬的%s,取钱已完成，您现在账户余额：%s' % (username, bank[username]['money']))
        print("您的个人信息如下所示")
        print("------------个人信息------------")
        print("用户名:%s" % (username))
        print("账号:%s" % (account))
        print("余额:%s" % (bank[username]['money']))
        print("开户行名称:%s" % (bank_name))
        print("------------山海银行-----------")
def quqian():#定义一个方法 #取款
        username = input("请输入用户名")
        password = input("请输入您的密码")
        account = input("请输入您的账号")
        c = input("请输入您要取出的金额")
        yyds = bank_quqian(username,password,account,c)
        if yyds == 1:
            print("账号不存在")
        elif yyds == 2:
            print("您输入的密码不对")

# 转账
def zhuanzhang():#转账
    rumoney = 0
    while 1:
        username = input("请输入要转出用户名")
        accountout = input("请输入要转出的账号")
        accountin = input("请输入要转入的账号")
        inuser = input("请输入要转入的用户名")
        password = input("请输入要转出的账号密码")
        n = input("请输入转账金额")
        if username not in bank:
            print("用户名不存在")
            return False
        if username == inuser:
            print("不能自己转给自己")
            break
        if n.isdigit():
            if int(n) <= bank[username]['money']:
                print("可以进行转账")
                bank[username]['money'] -= int(n)
                rumoney += int(n)
                print('尊敬的%s,转账已完成，您现在账户余额：%s' % (username, bank[username]['money']))
                print("亲爱的%s,您的账户已经入账：%s" % (inuser,rumoney))
                print("------------个人信息------------")
                print("用户名:%s" % (username))
                print("转入账号:%s" % (accountin))
                print("转出账号:%s" % (accountout))
                print("转出账号密码:%s" % (password))
                print("余额:%s" % (bank[username]['money']))
                print("开户行名称:%s" % (bank_name))
                print("------------山海银行-----------")
                break
            else:
                print("钱不够，无法转账")
                print("请重新进行转账操作")



def chaxun():
    while 1:
        username = input("请输入用户名")
        account = input("请输入您的账号")
        password = input("请输入您的密码")
        if username not in bank:
            print("该用户不存在")
        elif bank[username]['password'] != password:
            print("您输入的密码不正确")
        else:
            print("------------个人信息------------")
            print("用户名:%s" % (username))
            print("当前账号:%s" % (account))
            print("密码:%s" % (password))
            print("余额:%s" % (bank[username]['money']))
            print("开户行名称:%s" % (bank_name))
            print("------------山海银行-----------")
            break
while True:
    begin = input("请选择业务")
    if begin =="1":#您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        addmoney()
    elif begin == "3":
        quqian()
    elif begin == "4":
        zhuanzhang()
    elif begin == "5":
        chaxun()
    else:
        print(6,"、退出")
        break

