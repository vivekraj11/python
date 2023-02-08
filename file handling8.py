fin=open('rhyme.txt','r')
print(type(fin))
count=0
content=fin.read()
print(type(content))
print(content)
vowel=['A','a','E','e','I','i','O','o','U','u']
for i in content:
    if i in vowel:
        count=count+1
        #print(i)
print(count)
