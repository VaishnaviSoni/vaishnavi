n=int(input())
f=1
if (n==0):
    print("1")
elif(n==1):
    print("1")
else:
    for i in range(2,n+1):
        f=f*i
print(f)
