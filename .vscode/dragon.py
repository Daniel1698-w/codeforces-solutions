s,n=list(map(int,input().split()))
li=[]
li2=[]
for i in range(n):
    curr=list(map(int,input().split()))
    li.append(curr[0])
    li2.append(curr[1])
while len(li)>0 and min(li)<s:
    x=li.index(min(li))
    s+=li2[x]
    del li2[x]
    li.remove(min(li))
if len(li)==0:
    print("YES")
else:
    print("NO")

