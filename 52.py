t=input().split()
a=t[0]
b=t[1]
s1=len(a)
s2=len(b)
if s2<=1000 and s1<=1000:
    if a==b:
        print(a)
    else:
        if s1>s2:
            print(a)
        elif s1<s2:
            print(b)
        else:
            print(a)
else:
    print("Invalid Input")
