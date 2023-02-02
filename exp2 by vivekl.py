def findmax(n,y=0):
    if n==0:
        return 0
    else:
        return max(findmax(n//10,0),n%10)
def finddiff(x,n):
    while(n!=0):
        print(x-n%10)
        x=n//10
print("max digit of number-341
      6 is :",findmax(3416))
print("max digit of number-1221 is :",findmax(1221))
print("max digit of number-9854 is :",findmax(9854))

