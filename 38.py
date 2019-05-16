n=int(input())
if n>0:
    a=list(map(int,input().split()))
    for i in range(0,n):
        print(a[i],i)
else:
    print("Invalid Input")
