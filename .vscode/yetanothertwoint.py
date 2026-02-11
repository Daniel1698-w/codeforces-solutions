t=int(input())
for i in range(t):
    a,b=list(map(int,input().split()))
    Max=abs(a-b)
    counter=0
    for i in range(10,0,-1):
        counter+= Max//i
        Max-=(Max//i) *i
    print(counter)

