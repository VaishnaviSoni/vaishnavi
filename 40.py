t1=input().split()
a1=int(t1[0])
a2=int(t1[1])
if a1<=60 and a2<=60:
    t2=input().split()
    b1=int(t2[0])
    b2=int(t2[1])
    print(abs(a1-b1),abs(a2-b2))
else:
    print("invalid")
