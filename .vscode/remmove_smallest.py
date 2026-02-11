t=int(input())
def check_it(lst):
    lst.sort()
    l=0
    r=1
    while r<len(lst):
        if abs(lst[r]-lst[l])>1:
            return "NO"
        r+=1
        l+=1
    return "YES"

for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    print(check_it(li))