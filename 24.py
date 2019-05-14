t=input().split()
n=int(t[0])
q=int(t[1])
if (n<=100000)and(q<=100000):
    for i in range(n+1,q):
        if (i%2)!=0:
            print(i,end=" ")
else:
    print("invalid")
        
