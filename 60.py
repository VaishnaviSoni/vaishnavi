import math
n=int(input())
def Log2(x): 
    if x==0: 
        return false
    return (math.log10(x)/math.log10(2))
def isPowe(n): 
    return (math.ceil(Log2(n))==math.floor(Log2(n)))
if(isPowe(n)): 
    print("yes")
else: 
    print("no")
