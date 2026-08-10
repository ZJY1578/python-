class Car:
    def __init__(self,c_brand ,c_color ,c_price ):
        self.brand = c_brand
        self.color = c_color
        self.price = c_price
c1 =Car("CXK","Red",100000)
print(c1.brand)
print(c1.color)
print(c1.price)
print(c1.__dict__)