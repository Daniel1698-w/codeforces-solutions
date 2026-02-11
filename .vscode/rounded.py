n = int(input())
for i in range(n):
    d = int(input())
    s =len(str(d))
    counter =0
    lst =[]
    for j in range(s):
        x = d%10
        d//=10
        if x == 0:
        
            continue
        else:
            counter += 1
            lst.append(x*pow(10,j))
    print(counter)
    for k in lst:
        print(k, end =" ")
