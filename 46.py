a=input()
s=len(a)
c=len(a)
if s<=1000:
    for i in range(s):
        if (a[i].isalpha() or a[i].isdigit()):
            c-=1
    print(c)
else:
    print("invalid")
