t=input().split()
a=int(t[0])
b=int(t[1])
if a<=100000 and b<=100000:
    c=a
    a=b
    b=c
    print(a,b)
else:
    print("Invalid")
