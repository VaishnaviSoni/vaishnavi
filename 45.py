a=input()
s=len(a)
c=0
if s<=1000:
    for i in a:
        if (i.isdigit()):
            c+=1
    print(c)
else:
    print("invalid")
