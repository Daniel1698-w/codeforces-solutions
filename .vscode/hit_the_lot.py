n=int(input())
li=[1,5,10,20,100]
counter=0
for i in range(4,-1,-1):
    counter+=n//li[i]
    n-=(n//li[i])*li[i]
print(counter)
