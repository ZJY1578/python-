#本案例用于输入一批商品信息(商品名 价格 数量) 优惠(优惠券 积分) 运费 计算订单总金额


def shop_object(*shop,coupon=0,score=0,express=0):
    total_price1 = 0
    for i in shop:
        total_price1 += i[1] * i[2]
    #只用优惠卷
    if total_price1 >= 5000 and coupon<=total_price1 and score == 0:
        total_price2 = total_price1 - coupon - score + express
        return total_price2
    #只用积分
    if total_price1 >= 5000 and coupon == 0 and score //100 <= total_price1:
        total_price3 = total_price1 - coupon - score//100 + express
        return total_price3
    #积分与优惠卷都用
    if total_price1 >= 5000 and coupon <= total_price1 and score // 100 <=total_price1:
        total_price4 = total_price1 - coupon - score // 100 +express
        return total_price4
    #不用优惠卷与积分
    else:
        return total_price1

ooo = shop_object(("鼠标",15000,2),("鼠",15000,2),("鼠",151100,2))
print(ooo)


