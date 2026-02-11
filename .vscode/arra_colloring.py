t=int(input())

for i in range(t):
    counter=0
    n=int(input())
    li=list(map(int,input().split()))
    for i in li:
        if i%2!=0:
            counter+=1
    if counter%2==0:
        print("YES")
    else:
        print("NO")