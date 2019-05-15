n=int(input())
if 1<=n<=100000:
    for i in range(0,n):
        arr=input().split()
        c=max(arr)
        print(c)
else:
    print("invalid")
