#Exp.1: Design a python program to do calculation of various operations
def add(a,b):
    return a+b
def diff(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b

print("1.Addition")
print("2.Difference")
print("3.Division")
print("4.Multiplication")
print("5.Exit")

while(1):
    opt=int(input("Enter OPTION: "))
    print(opt)
    if opt==1:
        print(add(10,6.3))
    elif opt==2:
        print(diff(6,7))
    elif opt==3:
        print(div(14,6))
    elif opt==4:
        print(mul(6,5))
    elif opt==5:
        break;
    else:
        print("Invalid Option")
print("THANK YOU")
