#exp-1b: Python function to find nPr and nCr
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def nPr(n,r):
    return fact(n)//fact(n-r)
def nCr(n,r):
    return nPr(n,r)//fact(r)
print("fact(6) is: ",fact(6))
print("nCr(6,5) is: ",nCr(6,5))
print("nPr(6,3) is: ",nPr(6,3))

