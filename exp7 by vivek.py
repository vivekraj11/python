class person():
    count=100
    def __init__(self,name,mobile):
        self.pid=person.count
        person.count+=1
        self.pname=name
        self.pmobile=mobile
    def Print(self):
        print(self.pid,self.pname,self.pmobile)
class cricketer(person):
    def __init__(self,name,mobile,tmatch,tscore):
        person.__init__(self,name,mobile)
        self.totalmatches=tmatch
        self.totalscore=tscore
    def Print(self):
        print(self.pid,self.pname,self.pmobile,self.totalmatches,self.totalscore)
class student(person):
    def __init__(self,name,mobile,semester,course):
        person.__init__(self,name,mobile)
        self.semester=semester
        self.course=course
    def Print(self):
        print(self.pid,self.pname,self.pmobile,self.semester,self.course)
class teacher(person):
    def __init__(self,name,mobile,design,salary):
        person.__init__(self,name,mobile)
        self.design=design
        self.salary=salary
    def Print(self):
        print(self.pid,self.pname,self.pmobile,self.design,self.salary)

t1=person('Vivek','8762570355')
t2=cricketer('Sachin','7788789800','280','11000')
t3=cricketer('Rohit','8809760087','220','8520')
t4=cricketer('Virat','7878988909','235','9720')
t5=student('Kabir','9876567890','VII','BTECH(CSE)')
t6=teacher('Sukhla Sir','9080706009','Prof.','44500pm')
t1.Print()
t2.Print()
t3.Print()
t4.Print()
t5.Print()
t6.Print()
