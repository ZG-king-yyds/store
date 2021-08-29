#随机抽取优惠券
import random
a=random.randint(0,2)
zheshu=["机械革命9折","卫龙辣条2折","老干妈1折"]
a=zheshu[a]
b=a
print("恭喜您选中：",a,"优惠券")

# 1.准备商品
shop = [
    ["机械革命",9000],  # shop[chose][1]
    ["Think pad",4500],
    ["Mac book pro",12000],
    ["洗衣坟",20],
    ["西瓜",2],
    ["老干妈",15],
    ["卫龙辣条",3.5]
]


# 2.准备足够的钱
money = input("请输入初始余额：")
money = int(money) # "5" --> 5
# 3.准备空的购物车
mycart = []
danjia = 0
danjia = float(danjia)

# 4.开始购物：
while True: # 死循环
    # 展示商品
    for key ,value in enumerate(shop):
        print(key,value)

    # 输入
    chose = input("请输入您想要的商品编号：")
    if chose.isdigit():# "5" --> 5
        chose = int(chose)
        # 商品是否存在
        if chose  > len(shop): # len()
            print("对不起，您输入商品不存在！")
        else:
            # 金钱是否足够
         if b=="机械革命9折":

            if chose == 0:
                if money < 8100:
                    print("穷鬼，钱不够!")
                else:
                  mycart.append(shop[chose])
                  money = money-8100

            else:
                  mycart.append(shop[chose])
                  money =  money - shop[chose][1]

         elif b=="卫龙辣条2折":

            if chose == 6:
                if money < 0.7:
                    print("穷鬼，钱不够!")
                else:
                    mycart.append(shop[chose])
                    money = money-0.7

            else:
                  mycart.append(shop[chose])
                  money = money - shop[chose][1]


         elif b=="老干妈1折":

            if chose == 5:
                if money < 3:
                    print("穷鬼，钱不够!")
                else:
                    mycart.append(shop[chose])
                    money = money - 3

            else:
                mycart.append(shop[chose])
                money = money - shop[chose][1]

         print("恭喜您，成功添加购物车!,您的余额还剩：", money, "￥")

    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，输入非法，请重新输入！")

# 打印购物小条
print("以下是您的购物小票，请拿好：")
print("--------------山海城----------------------")
for key ,value in enumerate(mycart):
    print(key,value)

print("您的钱包余额还剩：",money,"￥")
print("-----------欢迎下次光临---------------------")