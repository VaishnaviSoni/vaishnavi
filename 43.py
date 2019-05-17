a=input()
s=len(a)
c=0
if s<=1000:
    for i in range(s):
        if a[i]==' ':
            c+=1
    print(c)
else:
    print("invalid")
