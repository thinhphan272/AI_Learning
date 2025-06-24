from abc import ABC, abstractmethod

import math

class Hinh(ABC):
    @abstractmethod
    def chuVi(self):
        pass
    
    @abstractmethod
    def dienTich(self):
        pass
    
    
class Circle(Hinh):
    def __init__(self, r):
        self.r = r
        
    def chuVi(self):
        return round(2 * math.pi * self.r, 2)
    
    def dienTich(self):
        return round(math.pi * self.r * self.r ,2)
    

class Rectangle(Hinh):
    def __init__(self, cd, cr):
        self.cd = cd
        self.cr = cr
        
    def chuVi(self):
        return (self.cd + self.cr) * 2
    
    def dienTich(self):
        return self.cd * self.cr
    

class Triagle(Hinh):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def chuVi(self):
        return self.a + self.b + self.c
    
    def dienTich(self):
        
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
    
    
ht1 = Circle(5)
print("Hình tròn:")
print(f"Dien tich: {ht1.dienTich()}")
print(f"Chuvi: {ht1.chuVi()}")


rect1 = Rectangle(7,9)
print("Hình chữ nhật:")
print(f"Dien tich: {rect1.dienTich()}")
print(f"Chuvi: {rect1.chuVi()}")

tri1 = Triagle(3, 4, 5)
print("Hình tam giác:")
print(f"Dien tich: {tri1.dienTich()}")
print(f"Chuvi: {tri1.chuVi()}")
























