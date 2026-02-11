str1=list(input())
str2=list(input())
str3=list(input())
str4=str1+str2
str4.sort()
str3.sort()
if len(str4)!=len(str3) or str3!=str4:
    print("NO")
else:
    print("YES")