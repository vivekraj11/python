class complex():
    def __init__(self,r=0,i=0):
        self.real=r
        self.img=i
    def display(self):
        print(self.real,"+",self.img,"i")
    def __add__(self,c2):
        x1=self.real+c2.real
        x2=self.img+c2.img
        return complex(x1,x2)
    def __gt__(self,cn):
        if self.real>cn.real:
            return True
        elif self.real==cn.real:
            if self.img>cn.img:
                return True
            else:
                return False
        else:
            return False
c1=complex(6,8)
c2=complex(5,2)
c3=c1+c2
c1.display()
c2.display()
c3.display()
        
