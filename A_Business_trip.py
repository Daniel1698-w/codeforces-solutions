k=int(input())
li=list(map(int,input().split()))
if k<=0:
    print(0)
else:
    li.sort()
    Sum=0
    counter=0
    r=len(li)-1
    while Sum<k and r>=0:
        Sum+=li[r]
        counter+=1
        r-=1
    if Sum<k:
        print(-1)
    else:
        print(counter)

