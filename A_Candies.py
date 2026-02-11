t=int(input())
for i in range(t):
    n=int(input())
    Sum=3
    k=2
    while n/Sum!= n//Sum:
        k+=1
        Sum=2**k -1
    print(n//((2**(k))-1))