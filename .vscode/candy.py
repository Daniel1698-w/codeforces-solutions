n = int(input())
for i in range(n):
    d = int(input())
    if d%2==0:
        print(int(d/2 -1))
    else:
        print(d//2)
