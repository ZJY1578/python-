print("欢迎使用购物车系统")
print("########## 购物车系统 ##########")
print("#                            #")
print("#        1. 添加购物车        #")
print("#        2. 修改购物车        #")
print("#        3. 删除购物车        #")
print("#        4. 查询购物车        #")
print("#        5. 退出购物车       #")
print("#        6.查看全部购物       #")
print("#        7.计算总金额         #")
print("##############################")
shoppiing_bk = {}
while True:
    allprice = 0
    act = input("请输入执行编号:")

#添加购物车操作
    match act:
        case "1":
            shopping_name = input("请输入商品名称")
            shopping_price = float(input("请输入商品价格"))
            shopping_num = float(input("请输入商品数量"))
            if shopping_name in shoppiing_bk:
                print("商品已存在")
            else:
                shoppiing_bk[shopping_name] = {"价格": shopping_price, "数量": shopping_num}



#修改购物车操作
        case"2":
            shopping_name = input("请输入要修改的商品名称")
            shopping_price = float(input("请输入要修改的商品价格"))
            shopping_num = float(input("请输入要修改的商品数量"))
            if shopping_name not in shoppiing_bk:
                print("该商品不在购物车中")
            else:
                print("修改成功")
                shoppiing_bk[shopping_name] = {"价格": shopping_price, "数量": shopping_num}
                print(shoppiing_bk)




#删除购物车操作
        case"3":
            shopping_name = input("请输入要删除的商品")
            if shopping_name not in shoppiing_bk:
                print("该商品不在购物车中")
            else:
                del shoppiing_bk[shopping_name]
                print("商品成功删除")







#购物车查询操作
        case"4":
            shopping_name = input("请输入要查询的商品")
            if shopping_name not in shoppiing_bk:
                print("该商品不在购物车中")
            else:
                print("商品名称",shopping_name,shoppiing_bk[shopping_name])



#退出操作
        case"5":
            print("正在退出 欢迎下次使用")
            break


#查看购物车
        case "6":
            for name,q in shoppiing_bk.items():
                print("商品名称",name,"商品价格",q["价格"],"商品数量",q["数量"])

#计算总金额
        case"7":
            for name,info in shoppiing_bk.items():
                allprice += info["价格"] * info["数量"]
            print(allprice)
        case _:
            print("请输入1到7的数字")
