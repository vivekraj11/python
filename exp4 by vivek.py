#exp 4 : WAPP to return sum of odd and even numbers of a list by writing esparate function to test odd and even
def evenn(n):
    if n%2==0:
        return True
    else:
        return False
def oddn(n):
    if n%2==1:
        return True
    else:
        return False
def soddeven(l):
    esum=0
    osum=0
    for i in l:
        if evenn(i)==True:
            esum=esum+i
        #elif oddn(i)==True:
        else:
            osum=osum+i
    return esum,osum
def main():
    l=[0,0,0,0,0]
    s=int(input("size: "))
    for i in range(s):
        l[i]=int(input("Number: "))
        print(soddeven(l))
main()
