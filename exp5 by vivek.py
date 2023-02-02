#WAP of python to find the sum and diffference of length() using class
class length():
    def __init__(self,c=0,m=0):
        self.cms=c
        self.mms=m
    def display(self):
        print(self.cms,"cm",self.mms,"mm")
    def add(self,l2,l3):
        self.cms=l2.cms+l3.cms
        self.mms=l2.mms+l3.mms
        if self.mms>=10:
            self.cms=self.cms+1
            self.mms=self.mms-10
    def getl(self):
        self.cms=int(input("Enter cm value:"))
        self.mms=int(input("Enter mm value:"))
    def compare(self,l2,l3):
        if l2.cms>l3.cms:
            return True
        elif l2.cms==l3.cms:
            if l2.mms>l3.mms:
                return True
            else:
                return False
        else:
            return False
    def difference(self,l1,l2):
        if l2.mms>l1.mms:
            self.mms=l1.mms+10-l2.mms
            self.cms=l1.cms-l2.cms-1
        else:
            self.cms=l1.cms-l2.cms
            self.mms=l1.mms-l2.mms
        print("Difference: ")
        self.display()
l1=length()
l1.display()
l2=length()
l3=length()
l2.getl()
l3.getl()
l1.add(l2,l3)
print("Addition: ")
l1.display()

