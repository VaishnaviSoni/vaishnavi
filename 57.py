n=int(input())
if n>=1:
    s=list(map(int,input().split()))
    print(min(s),max(s))
else:
    print("Invalid Input")
