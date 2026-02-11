n=int(input())
counter=0
for i in range(n):
    a,b=list(map(int,input().split()))
    if abs(a-b)>=2:
        counter+=1
print(counter)
