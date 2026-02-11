n=int(input())
x=n+1
while len(str(x))!=len(set(str(x))):
    x+=1
print(x)