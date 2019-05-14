n=int(input())
if(n==1):
    print("no")
elif(n==2):
    print("yes")
for i in range(2,n):
    if (n%i)==0:
        print("no")
        break
else:
    print("yes")

