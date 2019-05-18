n=input()
c=0
if len(n)<=100000000000:
    for i in range(0,len(n)):
        if n[i].isdigit():
            c+=1
    print(c)
else:
    print("invalid")
