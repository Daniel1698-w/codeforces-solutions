h,m=map(int,input().split(':'))
h1,m1=map(int,input().split(':'))
if h1>h or (h1==h and m1>m):
    h=24+h
x=h1*60+m1
x1=h*60+m
cx=x1-x
h3=cx//60
m3=int(cx%60)
ah=str(h3)
am=str(m3)
if h3//10==0:
    ah='0'+str(h3)
if m3//10==0:
    am='0'+str(m3)
print(ah+":"+am)