t=int(input())
for i in range(t):
    li=list(map(int,input().split()))
    Timur=li[0]
    li.sort()
    print(3-li.index(Timur))