t=int(input())



for i in range(t):
    a,b=list(map(int,input().split()))
    if a%b==0:
        print(0)
    else:
        x=a//b +1
        print(x*b-a)

    