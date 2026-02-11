n=int(input())
li=list(map(int,input().split()))
li.sort()
counter=li.count(4)
print(f"counter = {counter}")
counter2=li.count(2)
counter+=counter2//2
print(f"counter = {counter} counti = {counter//2}")
counter2-=(counter2//2)*2
counter3=li.count(3)
counter1=li.count(1)
m13=min(counter1,counter3)
counter+=m13
print(f"counter = {counter} ,  m13 = {m13}")
counter1-=m13
counter3-=m13
counter+=counter3
print(f"counter = {counter}")
m12=min(counter1//2,counter2)
print(f" c1 = {counter//2} , counter2 = {counter2}")
counter+=m12
print(f"counter = {counter}  , m12 = {m12}")
counter1-= 2*m12
counter2-=m12

m12=min(counter1,counter2)
counter+=m12
counter1-=m12
counter2-=m12
print(f" m12 now ={m12} , counter = {counter}")
counter+=counter2

counter+=counter1//4
counter1-=4*(counter1//4)

counter+=counter1//3
counter1-=3*(counter1//3)

counter+=counter1//2
counter1-=2*(counter1//2)

counter+=counter1
print(f"counter = {counter}")

print(counter)

