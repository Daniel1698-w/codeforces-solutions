n=int(input())
li=list(map(int,input().split()))
li2=li.copy()
Max=max(li)
Min=min(li)

x_max=li.index(Max)
for i in range(x_max,0):
    li[i],li[i-1]=li[i-1],li[i]


# x_min=li[::-1].index(Min)
x_min=len(li)-1-li.index(Min)
maxx=x_max+x_min


x_min2=li2[::-1].index(Min)

for i in range(li2.index(Min),n-1):
    li2[i],li2[i+1]=li2[i+1],li2[i]

x_max2=li2.index(Max)
maxx2=x_min2+x_max2
print(min(maxx2,maxx))
