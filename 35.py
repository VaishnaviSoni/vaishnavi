n=int(input())
if 1<=n<=1000:
    a=list(map(int,input().split()))
    c=(a[0]+a[n-1])//2
    print(c)
else:
    print("invalid")
