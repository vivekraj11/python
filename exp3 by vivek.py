#use any built in function for a list
def fun(n,z):
    i=0
    y=len(n)
    x=[]
    while(i!=y):
        i=n.index(z,i,y)
        x.append(i)
        i=i+1
    print(x)
def main():
    n=[]
    i=int(input("Enter no. of elements: "))
    while(i!=0):
        x=int(input())
        n.append(x)
        i=i-1
        z=int(input("Enter variable: "))
        fun(n,z)
main()

