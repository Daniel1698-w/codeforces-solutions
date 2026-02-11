import math
x=int(input())
def is_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True
if x<6:
    print(0)
elif x==6:
    print(1)
else:
    prime=0
    for i in range(2,x+1):
        if is_prime(i):
            prime+=1
    squares=int(math.sqrt(x))-1
    print(f"prime ={prime} , squares = {squares})
