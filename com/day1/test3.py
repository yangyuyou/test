li=["电脑","鼠标","游艇","美女"]
for i in range(len(li)):
    print

goods_list=[
    {"name":"电脑","price":1999},
    {"name":"鼠标","price":10},
    {"name":"游艇","price":20},
    {"name":"美女","price":988},
]
shopping_list=[]
for i,j in enumerate(goods_list,1):
    print(i,j["name"],j["price"])
total_assets=input("请输入你的总资产")
total_money=int(total_assets)
while True:
    inp=input("请输入购买商品的序号，结束购买请按0，查看购物车请按9")
    if int(inp)==1:
        shopping_list.append(goods_list[int(inp)-1])
    elif int(inp)==2:
        shopping_list.append(goods_list[int(inp)-1])
    elif int(inp)==3:
        shopping_list.append(goods_list[int(inp) - 1])
    elif int(inp)==4:
        shopping_list.append(goods_list[int(inp) - 1])
    elif int(inp) == 9:

        while True:
            inp=input("请输入要移除商品的序号，结束请按0")
            if int(inp) == 1:
                shopping_list.append(goods_list[int(inp) - 1])
                print(shopping_list)
            elif int(inp) == 2:
                shopping_list.append(goods_list[int(inp) - 1])
                print(shopping_list)
            elif int(inp) == 3:
                shopping_list.append(goods_list[int(inp) - 1])
                print(shopping_list)
            elif int(inp) == 4:
                shopping_list.append(goods_list[int(inp) - 1])
                print(shopping_list)
            elif int(inp) == 0:
                break
            else:
                print("请输入正确的商品序号")
    elif int(inp) == 0:
        break
    else:
        print("请输入正确的商品序号")
print(shopping_list)
sum1=0
for i in shopping_list:
    val=(i['price'])
    sum=int(val)
    sum1=sum1+sum
    print("购物总金额：",sum1)
    while True:
        if total_money>=sum1:
            inp=input("请按1确认购买")
            if int(inp)==1:
                total_money=total_money-sum1
                print("购买成功")
                print("剩余资产：",total_money)
                sum1=0
                break
            else:
                inp=input("金额不足输入1进行充值，输入其他取消购买")
                if int(inp)==1:
                    inp=input("请输入充值金额")
                    total_money=total_money+int(inp)
                    print("总资产：",total_money)
                    continue
                else:
                    print("取消购买")
                    break







