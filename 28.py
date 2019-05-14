r=input().split()
a=int(r[0])
b=int(r[1])
for n in range(a+1,b):
    s=0  
    t=n
    if n<=100000:
        while(t>0):  
           digit = t%10  
           s+= digit ** 3  
           t//=10  
        if (n==s):  
           print(n,end=" ")
           
    else:
        print("invalid")
