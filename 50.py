n=int(input())
n1=1
n2=1
c=0
if n<=0:
    print("Invalid input")
elif n==1:
    print(n1)
elif n==2:
    print(n2)
else:
    while c<n:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1
        
