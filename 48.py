t=input().split()
a=int(t[0])
b=int(t[1])
if a<=100000 and b<=100000:
    a=a^b
    b=a^b
    a=a^b
    print(a,b)
else:
    print("Invalid")
