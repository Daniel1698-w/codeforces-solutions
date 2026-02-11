n=int(input())
x=0
Max=0
for i in range(n):
    a,b=list(map(int,input().split()))
    x+=b-a
    Max=max(Max,x)
print(Max)
