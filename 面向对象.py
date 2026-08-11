# class Car:
#     def __init__(self,c_brand ,c_color ,c_price ):
#         self.brand = c_brand
#         self.color = c_color
#         self.price = c_price
# c1 =Car("CXK","Red",100000)
# print(c1.brand)
# print(c1.color)
# print(c1.price)
# print(c1.__dict__)

class Phone:
    def __init__(self,p_color,p_number,p_ver,p_price ):
        self.color = p_color
        self.number = p_number
        self.ver = p_ver
        self.price = p_price
        print("添加完毕")




    def run1 (self):
        print(f"{self.color},{self.number},{self.ver}运行中")



    def cost (self,discont,rate):
        cost = (self.price * self.number * discont) + (self.price * self.number * rate)
        return cost

c1 = Phone("red",114514,"17ProMax",19999)
c1.run1()
totalcost = c1.cost(discont=10,rate=5)
print(totalcost)