n=int(input())
if n>=1:
    s=list(map(int,input().split()))
    print(sum(s)//n)
else:
    print("Invalid Input")
