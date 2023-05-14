import math

class triangle_area: 
    def __init__(self, base, height, is_right = False):
        self.base = base
        self.height = height
        self.is_right = is_right
        
    def hypotenuse(self, length):
        if(self.is_right == True):
            self.length = sqrt(self.base^2 + self.height^2)
        else:
            print("This is not a right triangle!")
    
    def area(self):
        a = (1/2)(self.base*self.height)
        if(self.base > 0 and self.height > 0):
            return a
        else:
            return 0

    def check():
        t1 = triangle_area(3,4,True)
        t1.hypotenuse()
        t1.area()
        
        t2 = triangle_area(4,10,False)
        t2.hypotenuse()
        t2.area()
        
        return t1,t2
    
if __name__ == "__main__": 
    triangle_area.check()