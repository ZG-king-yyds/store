import random
num=random.randint(0, 11)
print(num)
i=int(100)
while 1:
    i=i-10
    a=input("请输入一个数字")
    a= int(a)
    if num > a:
        print("猜小了")
    elif num < a:
        print("猜大了")
    elif  num == a :
        print("回答正确，游戏结束,所剩资金为",i)
        break
    if i == 0:
           print("游戏结束，所剩资金为0")
           break