t=input().split()
n=int(t[0])
a=int(t[1])
d=int(t[2])
s=0
if 1<=n<=100000 and 1<=a<=100000 and 1<=d<=100000:
    s=(n/2)*((2*a)+(n-1)*d)
    print(int(s))
else:
    print("invalid")
