#include<stdio.h>
int main(){
    int t,n,rev=0;
    scanf("%d",&n);
    t=n;
    while(t!=0){
        rev=rev*10;
        rev=rev+t%10;
        t=t/10;
    }
    if (n==rev)
        printf("yes");
        else
        printf("no");
        return 0;
}
