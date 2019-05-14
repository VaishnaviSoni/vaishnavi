n=int(input())  
s=0  
t=n
if n<=100000:
    while(t>0):  
       digit = t%10  
       s+= digit ** 3  
       t//=10  
    if (n==s):  
       print("yes")  
    else:  
       print("no") 
else:
    print("invalid")
